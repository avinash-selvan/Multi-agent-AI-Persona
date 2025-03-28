import os
import json
from datetime import datetime
from abc import ABC, abstractmethod
from typing import Dict, Any
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from config import OLLAMA_MODEL, ENABLE_AGENT_LOGGING, DEBUG_MODE
import traceback
from memory import LogManager


class BaseAgent(ABC):
    def __init__(self, name: str, prompt_template: str):
        self.name = name
        self.llm = OllamaLLM(model=OLLAMA_MODEL, temperature=0.7)
        self.prompt = PromptTemplate(
            input_variables=['user_input', 'memory', 'user_profile'],
            template=prompt_template
        )
        self.chain = self.prompt | self.llm
        self.log_file_path = f"logs/agent_logs.jsonl"
        self.logger = LogManager()

        # Ensure logs directory exists
        os.makedirs(os.path.dirname(self.log_file_path), exist_ok=True)

    @abstractmethod
    def process_input(self, 
                      user_input: str, 
                      memory: Dict[str, Any], 
                      user_profile: Dict[str, Any]) -> str:
        pass

    def generate_response(self, 
                          user_input: str, 
                          memory: Dict[str, Any], 
                          user_profile: Dict[str, Any]) -> str:
        try:
            response = self.chain.invoke({
                "user_input": user_input,
                "memory": json.dumps(memory, indent=2),
                "user_profile": json.dumps(user_profile, indent=2)
            })

            # ✅ Log agent interaction
            self.logger.append_log({
                "agent": self.name,
                "input": user_input,
                "memory": memory,
                "user_profile": user_profile,
                "response": response,
                "timestamp": datetime.now().isoformat()
            })

            return response

        except Exception as e:
            error_details = traceback.format_exc()

            # ✅ Log the error
            self.logger.append_log({
                "agent": self.name,
                "error": str(e),
                "trace": error_details,
                "input": user_input,
                "timestamp": datetime.now().isoformat()
            })

            print(f"Error in {self.name} agent: {e}")
            return f"⚠️ {self.name} encountered an error: {e}"

    def _log_interaction(self, input_data: Dict[str, Any], response: str = None, error: str = None):
        if not ENABLE_AGENT_LOGGING:
            return

        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "agent": self.name,
            "input": input_data,
            "response": response,
            "error": error
        }

        if DEBUG_MODE:
            print(f"[DEBUG] Logging agent interaction: {log_entry}")

        with open(self.log_file_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(log_entry) + "\n")


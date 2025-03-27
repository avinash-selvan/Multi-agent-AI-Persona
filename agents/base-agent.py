from abc import ABC, abstractmethod
from typing import Dict, Any
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

class BaseAgent(ABC):
    def __init__(self, name: str, prompt_template: str):
        """
        Initialize base agent with a name and prompt template.
        
        TODO: 
        - Replace OpenAI with your preferred LLM (e.g., Claude, GPT-4)
        - Add API key configuration
        """
        self.name = name
        self.llm = OpenAI(temperature=0.7)  # Adjust temperature as needed
        self.prompt = PromptTemplate(
            input_variables=['user_input', 'memory', 'user_profile'],
            template=prompt_template
        )
        self.chain = LLMChain(llm=self.llm, prompt=self.prompt)

    @abstractmethod
    def process_input(self, 
                      user_input: str, 
                      memory: Dict[str, Any], 
                      user_profile: Dict[str, Any]) -> str:
        """
        Process user input with agent-specific logic.
        
        Args:
            user_input: Current user reflection
            memory: Recent log history
            user_profile: User's profile information
        
        Returns:
            Agent's response
        """
        pass

    def generate_response(self, 
                           user_input: str, 
                           memory: Dict[str, Any], 
                           user_profile: Dict[str, Any]) -> str:
        """
        Generate response using LLM chain.
        
        TODO: 
        - Add error handling
        - Implement logging of agent interactions
        """
        try:
            response = self.chain.run(
                user_input=user_input,
                memory=memory,
                user_profile=user_profile
            )
            return response
        except Exception as e:
            print(f"Error in {self.name} agent: {e}")
            return f"I encountered an error processing the input: {e}"

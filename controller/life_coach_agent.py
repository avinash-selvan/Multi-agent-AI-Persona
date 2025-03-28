from typing import List, Dict, Any
from agents import WarriorAgent, MonkAgent, MillionaireAgent
from langchain_ollama import OllamaLLM
from memory import UserProfileManager, LogManager
from datetime import datetime

class LifeCoachAgent:
    def __init__(self):
        """
        Initialize Life Coach with persona agents and memory managers.
        
        TODO:
        - Add configuration for agent order/toggling
        - Implement more sophisticated routing logic
        """
        self.agents = [
            WarriorAgent(),
            MonkAgent(), 
            MillionaireAgent()
        ]
        self.profile_manager = UserProfileManager()
        self.log_manager = LogManager()

    def process_reflection(self, user_input: str, full_council_mode: bool = True) -> Dict[str, Any]:
        """
        Process user reflection through multiple agents.
        
        Args:
            user_input: User's hourly self-reflection
            full_council_mode: Toggle between full persona responses or summary
        
        Returns:
            Dictionary with persona responses and summary
        """
        # Retrieve user profile and recent logs
        user_profile = self.profile_manager.load_profile()
        recent_logs = self.log_manager.get_recent_logs(limit=3)

        # Generate responses from each agent
        agent_responses = {}
        for agent in self.agents:
            response = agent.process_input(
                user_input, 
                memory=recent_logs, 
                user_profile=user_profile
            )
            agent_responses[agent.name.lower()] = response

        # Generate summary (TODO: Implement more sophisticated summary generation)
        summary = self._generate_summary(agent_responses)
        agent_responses['summary'] = summary

        # Log the interaction
        self.log_manager.append_log({
            'timestamp': datetime.now().isoformat(),
            'entry': user_input,
            'responses': agent_responses
        })

        # Return full or summary mode based on configuration
        return agent_responses if full_council_mode else {'summary': summary}

    def _generate_summary(self, agent_responses: Dict[str, str]) -> str:
        """
        Generate a concise summary of agent responses.
        
        TODO:
        - Implement more intelligent summarization
        - Add sophisticated NLP techniques for summary generation
        """
        summary_prompt = f"""
        Summarize the following agent perspectives concisely:
        Warrior: {agent_responses.get('warrior', '')}
        Monk: {agent_responses.get('monk', '')}
        Millionaire: {agent_responses.get('millionaire', '')}

        Create a holistic, actionable summary.
        """
        # Use an LLM to generate summary (placeholder)
        summary_generator = OllamaLLM(model='mistral',temperature=0.5)
        return summary_generator.invoke(summary_prompt)

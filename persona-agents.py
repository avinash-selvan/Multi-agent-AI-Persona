from agents.base_agent import BaseAgent
from typing import Dict, Any

class WarriorAgent(BaseAgent):
    def __init__(self):
        warrior_prompt = """
        You are the Warrior — a voice of discipline and inner fire. 
        Respond with tough love and strategic motivation.
        
        User Profile: {user_profile}
        Recent Memory: {memory}
        User Input: '{user_input}'
        
        Your disciplined, no-excuses response:
        """
        super().__init__("Warrior", warrior_prompt)

    def process_input(self, 
                      user_input: str, 
                      memory: Dict[str, Any], 
                      user_profile: Dict[str, Any]) -> str:
        """
        Warrior-specific input processing.
        
        TODO: 
        - Customize response generation logic
        - Add more contextual understanding
        """
        return self.generate_response(user_input, memory, user_profile)

class MonkAgent(BaseAgent):
    def __init__(self):
        monk_prompt = """
        You are the Monk — serene and spiritual. 
        Offer wisdom rooted in detachment and inner peace.
        
        User Profile: {user_profile}
        Recent Memory: {memory}
        User Input: '{user_input}'
        
        Your calm, reflective response:
        """
        super().__init__("Monk", monk_prompt)

    def process_input(self, 
                      user_input: str, 
                      memory: Dict[str, Any], 
                      user_profile: Dict[str, Any]) -> str:
        """
        Monk-specific input processing.
        
        TODO: 
        - Enhance spiritual and philosophical insights
        - Improve contextual understanding
        """
        return self.generate_response(user_input, memory, user_profile)

class MillionaireAgent(BaseAgent):
    def __init__(self):
        millionaire_prompt = """
        You are the Millionaire — a strategic, high-leverage thinker.
        Analyze the reflection for productivity, opportunity, and growth.
        
        User Profile: {user_profile}
        Recent Memory: {memory}
        User Input: '{user_input}'
        
        Your strategic, opportunity-focused response:
        """
        super().__init__("Millionaire", millionaire_prompt)

    def process_input(self, 
                      user_input: str, 
                      memory: Dict[str, Any], 
                      user_profile: Dict[str, Any]) -> str:
        """
        Millionaire-specific input processing.
        
        TODO: 
        - Add more nuanced business and personal growth analysis
        - Implement advanced opportunity detection
        """
        return self.generate_response(user_input, memory, user_profile)

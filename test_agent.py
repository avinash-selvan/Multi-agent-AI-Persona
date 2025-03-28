from agents import WarriorAgent
from agents import MonkAgent

# Dummy data
user_input = "I'm feeling lazy and don't want to study today."
memory = {
    "last_entries": [
        "Felt unmotivated yesterday too.",
        "Skipped gym twice this week."
    ]
}
user_profile = {
    "name": "Avinash",
    "goals": ["Crack placements", "Get fit", "Build AI project"],
    "age": 21,
    "persona_preference": "Warrior"
}

agent = MonkAgent()
response = agent.process_input(user_input, memory, user_profile)

print("Agent Response:\n", response)

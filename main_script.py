from controller.life_coach_agent import LifeCoachAgent
from datetime import datetime

def main():
    """
    Main application entry point.
    
    TODO:
    - Add CLI or UI interface
    - Implement more robust user interaction
    """
    life_coach = LifeCoachAgent()

    # Example usage
    while True:
        user_input = input("Enter your hourly reflection (or 'quit' to exit): ")
        
        if user_input.lower() == 'quit':
            break
        
        # Process reflection with full council mode
        responses = life_coach.process_reflection(user_input)
        
        # Display responses
        print("\n--- Warrior's Perspective ---")
        print(responses['warrior'])
        
        print("\n--- Monk's Perspective ---")
        print(responses['monk'])
        
        print("\n--- Millionaire's Perspective ---")
        print(responses['millionaire'])
        
        print("\n--- Summary ---")
        print(responses['summary'])

if __name__ == "__main__":
    main()

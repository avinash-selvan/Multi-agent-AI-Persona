import json
from typing import Dict, Any
from pathlib import Path
from datetime import datetime

class UserProfileManager:
    def __init__(self, profile_path: str = 'user_profile.json'):
        """
        Manage user profile loading and saving.
        
        TODO:
        - Add profile validation
        - Implement more robust error handling
        """
        self.profile_path = Path(profile_path)
        
        # Create default profile if not exists
        if not self.profile_path.exists():
            self._create_default_profile()

    def load_profile(self) -> Dict[str, Any]:
        """
        Load user profile from JSON file.
        
        Returns:
            User profile dictionary
        """
        try:
            with open(self.profile_path, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading profile: {e}")
            return self._create_default_profile()

    def save_profile(self, profile: Dict[str, Any]):
        """
        Save updated user profile.
        
        TODO:
        - Add profile schema validation
        - Implement backup mechanism
        """
        try:
            with open(self.profile_path, 'w') as f:
                json.dump(profile, f, indent=2)
        except Exception as e:
            print(f"Error saving profile: {e}")

    def _create_default_profile(self) -> Dict[str, Any]:
        """
        Create a default user profile.
        
        Returns:
            Default profile dictionary
        """
        default_profile = {
            "name": "User",
            "goals": [],
            "values": [],
            "struggles": [],
            "personality": None,
            "created_at": datetime.now().isoformat()
        }
        self.save_profile(default_profile)
        return default_profile

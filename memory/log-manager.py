import json
from typing import List, Dict, Any
from pathlib import Path
from datetime import datetime, timedelta

class LogManager:
    def __init__(self, log_path: str = 'logs.json'):
        """
        Manage logging of user interactions.
        
        TODO:
        - Implement log rotation
        - Add more sophisticated log management
        """
        self.log_path = Path(log_path)
        
        # Create logs file if not exists
        if not self.log_path.exists():
            with open(self.log_path, 'w') as f:
                json.dump([], f)

    def append_log(self, log_entry: Dict[str, Any]):
        """
        Append a new log entry to the logs file.
        
        Args:
            log_entry: Dictionary containing log information
        """
        try:
            with open(self.log_path, 'r+') as f:
                logs = json.load(f)
                logs.append(log_entry)
                
                # Optional: Limit log size
                logs = logs[-100:]  # Keep last 100 entries
                
                f.seek(0)
                json.dump(logs, f, indent=2)
                f.truncate()
        except Exception as e:
            print(f"Error appending log: {e}")

    def get_recent_logs(self, limit: int = 3, 
                        within_hours: int = 24) -> List[Dict[str, Any]]:
        """
        Retrieve recent logs.
        
        Args:
            limit: Maximum number of logs to return
            within_hours: Retrieve logs within specified hours
        
        Returns:
            List of recent log entries
        """
        try:
            with open(self.log_path, 'r') as f:
                logs = json.load(f)
            
            # Filter logs within time range
            current_time = datetime.now()
            recent_logs = [
                log for log in logs 
                if (current_time - datetime.fromisoformat(log['timestamp'])) 
                   < timedelta(hours=within_hours)
            ]
            
            # Sort and limit
            recent_logs.sort(key=lambda x: x['timestamp'], reverse=True)
            return recent_logs[:limit]
        
        except Exception as e:
            print(f"Error retrieving logs: {e}")
            return []

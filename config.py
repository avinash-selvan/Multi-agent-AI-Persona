import os
from dotenv import load_dotenv

load_dotenv()

# Language model
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral")

# Toggle agent interaction logging
ENABLE_AGENT_LOGGING = os.getenv("ENABLE_AGENT_LOGGING", "true").lower() == "true"

# Debug mode (optional)
DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"

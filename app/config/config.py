"""
Configuration loader for environment variables.
Reads API base URL and other settings from .env file.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    JSONPLACEHOLDER_BASE_URL = os.getenv("JSONPLACEHOLDER_BASE_URL")
    USER_CSV_PATH = os.getenv("USER_CSV_PATH")
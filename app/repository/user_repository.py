"""
Repository layer for fetching users from JSONPlaceholder API.
"""

import requests
from typing import List, Any
from app.config.config import Config

class UserRepository:
    def __init__(self, base_url: str = None):
        self.base_url = base_url or Config.JSONPLACEHOLDER_BASE_URL

    def fetch_users(self) -> List[Any]:
        """
        Fetches users from the JSONPlaceholder API.
        Returns the raw list of user dicts.
        Raises requests.HTTPError on network or HTTP errors.
        """
        url = f"{self.base_url}/users"
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch users: {e}")
"""
Repository layer for fetching users from JSONPlaceholder API and persisting to CSV.
"""

import requests
import os
import csv
from typing import List, Any
from app.config.config import Config

class UserRepository:
    def __init__(self, base_url: str = None, csv_path: str = None):
        self.base_url = base_url or Config.JSONPLACEHOLDER_BASE_URL
        self.csv_path = csv_path or Config.USER_CSV_PATH

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

    def flatten_user(self, user: dict) -> dict:
        """
        Flattens a user dict, including nested address, geo, and company fields.
        """
        flat = {}
        # Top-level fields
        for key in ['id', 'name', 'username', 'email', 'phone', 'website']:
            flat[key] = user.get(key, "")
        # Address fields
        address = user.get('address', {})
        for key in ['street', 'suite', 'city', 'zipcode']:
            flat[f'address.{key}'] = address.get(key, "")
        geo = address.get('geo', {})
        flat['address.geo.lat'] = geo.get('lat', "")
        flat['address.geo.lng'] = geo.get('lng', "")
        # Company fields
        company = user.get('company', {})
        for key in ['name', 'catchPhrase', 'bs']:
            flat[f'company.{key}'] = company.get(key, "")
        return flat

    def get_csv_fieldnames(self, users: List[dict]) -> List[str]:
        """
        Returns the CSV fieldnames in the order as returned by the API.
        """
        # Use the first user as a template for field order
        if not users:
            raise ValueError("No users to determine CSV fieldnames.")
        flat = self.flatten_user(users[0])
        return list(flat.keys())

    def persist_users_to_csv(self, users: List[dict]) -> str:
        """
        Persists the list of user dicts to a CSV file.
        Returns the path to the CSV file.
        """
        import logging
        if not users:
            raise ValueError("No users to persist to CSV.")
        fieldnames = self.get_csv_fieldnames(users)
        os.makedirs(os.path.dirname(self.csv_path), exist_ok=True)
        try:
            with open(self.csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for user in users:
                    writer.writerow(self.flatten_user(user))
            logging.info(f"CSV successfully written to {self.csv_path}")
        except Exception as e:
            logging.error(f"Failed to write CSV: {e}")
            raise
        return self.csv_path
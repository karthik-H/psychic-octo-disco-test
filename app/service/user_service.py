"""
Service layer for user business logic and error handling.
"""

from typing import List
from app.repository.user_repository import UserRepository
from app.domain.models import User, Address, Company, Geo

class UserService:
    def __init__(self, user_repository: UserRepository = None):
        self.user_repository = user_repository or UserRepository()

    def get_all_users(self) -> List[User]:
        """
        Fetches and parses all users from the repository.
        Returns a list of User domain objects.
        Raises RuntimeError on fetch or parse errors.
        """
        raw_users = self.user_repository.fetch_users()
        return [self._parse_user(u) for u in raw_users]

    def _parse_user(self, data: dict) -> User:
        try:
            geo = Geo(
                lat=data["address"]["geo"]["lat"],
                lng=data["address"]["geo"]["lng"]
            )
            address = Address(
                street=data["address"]["street"],
                suite=data["address"]["suite"],
                city=data["address"]["city"],
                zipcode=data["address"]["zipcode"],
                geo=geo
            )
            company = Company(
                name=data["company"]["name"],
                catchPhrase=data["company"]["catchPhrase"],
                bs=data["company"]["bs"]
            )
            return User(
                id=int(data["id"]),
                name=data["name"],
                username=data["username"],
                email=data["email"],
                address=address,
                phone=data["phone"],
                website=data["website"],
                company=company
            )
        except (KeyError, TypeError, ValueError) as e:
            raise RuntimeError(f"Failed to parse user data: {e}")
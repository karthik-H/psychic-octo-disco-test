"""
Entrypoint/controller for fetching and displaying user data.
"""

import logging
from app.service.user_service import UserService

def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    user_service = UserService()
    try:
        users = user_service.get_all_users()
        logging.info(f"Fetched {len(users)} users.")
        for user in users:
            print(f"ID: {user.id}, Name: {user.name}, Username: {user.username}, Email: {user.email}, "
                  f"Phone: {user.phone}, Website: {user.website}")
            print(f"  Address: {user.address.street}, {user.address.suite}, {user.address.city}, {user.address.zipcode} "
                  f"(Geo: {user.address.geo.lat}, {user.address.geo.lng})")
            print(f"  Company: {user.company.name}, {user.company.catchPhrase}, {user.company.bs}")
            print("-" * 60)
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
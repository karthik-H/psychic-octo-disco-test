"""
Entrypoint/controller for fetching, displaying, and exporting user data to CSV.
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
        # Export to CSV
        csv_path = user_service.export_users_to_csv()
        logging.info(f"User data exported to CSV: {csv_path}")
    except Exception as e:
        logging.error(f"Error: {e}")

if __name__ == "__main__":
    main()
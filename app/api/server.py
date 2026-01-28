"""
Flask API server exposing /users endpoint with CORS and clean architecture integration.
"""

import logging
from flask import Flask, jsonify
from flask_cors import CORS
from app.service.user_service import UserService
from app.domain.models import User
import os

# Logging config
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

app = Flask(__name__)
CORS(app, resources={r"/users": {"origins": os.getenv("FRONTEND_ORIGIN", "*")}}, supports_credentials=True)

user_service = UserService()

@app.route("/users", methods=["GET"])
def get_users():
    try:
        users = user_service.get_all_users()
        # Convert dataclass objects to dicts for JSON serialization
        def user_to_dict(user: User):
            return {
                "id": user.id,
                "name": user.name,
                "username": user.username,
                "email": user.email,
                "phone": user.phone,
                "website": user.website,
                "address": {
                    "street": user.address.street,
                    "suite": user.address.suite,
                    "city": user.address.city,
                    "zipcode": user.address.zipcode,
                    "geo": {
                        "lat": user.address.geo.lat,
                        "lng": user.address.geo.lng
                    }
                },
                "company": {
                    "name": user.company.name,
                    "catchPhrase": user.company.catchPhrase,
                    "bs": user.company.bs
                }
            }
        return jsonify([user_to_dict(u) for u in users]), 200
    except Exception as e:
        logging.error(f"Error in /users: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.getenv("BACKEND_PORT", 5000))
    app.run(host="0.0.0.0", port=port)
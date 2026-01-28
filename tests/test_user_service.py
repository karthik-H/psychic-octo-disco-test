import pytest
from app.service.user_service import UserService
from app.domain.models import User

class MockUserRepository:
    def fetch_users(self):
        return [
            {
                "id": 1,
                "name": "Leanne Graham",
                "username": "Bret",
                "email": "Sincere@april.biz",
                "address": {
                    "street": "Kulas Light",
                    "suite": "Apt. 556",
                    "city": "Gwenborough",
                    "zipcode": "92998-3874",
                    "geo": {"lat": "-37.3159", "lng": "81.1496"}
                },
                "phone": "1-770-736-8031 x56442",
                "website": "hildegard.org",
                "company": {
                    "name": "Romaguera-Crona",
                    "catchPhrase": "Multi-layered client-server neural-net",
                    "bs": "harness real-time e-markets"
                }
            }
        ]

    def persist_users_to_csv(self, users):
        # Simulate CSV export
        return "/tmp/fake.csv"

def test_get_all_users_success():
    service = UserService(user_repository=MockUserRepository())
    users = service.get_all_users()
    assert isinstance(users, list)
    assert isinstance(users[0], User)
    assert users[0].id == 1
    assert users[0].name == "Leanne Graham"
    assert users[0].address.city == "Gwenborough"
    assert users[0].company.name == "Romaguera-Crona"

def test_get_all_users_parse_error():
    class BadRepo:
        def fetch_users(self):
            return [{"id": 1, "name": "Missing fields"}]  # Incomplete data

    service = UserService(user_repository=BadRepo())
    with pytest.raises(RuntimeError):
        service.get_all_users()

def test_export_users_to_csv():
    service = UserService(user_repository=MockUserRepository())
    csv_path = service.export_users_to_csv()
    assert csv_path == "/tmp/fake.csv"
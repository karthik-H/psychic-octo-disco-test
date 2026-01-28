import pytest
from app.repository.user_repository import UserRepository

def test_fetch_users_success(monkeypatch):
    class MockResponse:
        def raise_for_status(self): pass
        def json(self):
            return [{"id": 1, "name": "Test User", "username": "test", "email": "test@example.com",
                     "address": {"street": "A", "suite": "B", "city": "C", "zipcode": "D", "geo": {"lat": "0", "lng": "0"}},
                     "phone": "123", "website": "site", "company": {"name": "X", "catchPhrase": "Y", "bs": "Z"}}]
    def mock_get(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr("requests.get", mock_get)
    repo = UserRepository()
    users = repo.fetch_users()
    assert isinstance(users, list)
    assert users[0]["id"] == 1

def test_fetch_users_network_error(monkeypatch):
    def mock_get(*args, **kwargs):
        raise Exception("Network error")
    monkeypatch.setattr("requests.get", mock_get)
    repo = UserRepository()
    with pytest.raises(RuntimeError):
        repo.fetch_users()
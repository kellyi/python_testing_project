import pytest
from fastapi.testclient import TestClient

from python_testing_project.main import app


client = TestClient(app)


@pytest.mark.api
class TestGet:
    def test_read_root(self):
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"Hello": "World"}

    def test_read_item_with_integer_id(self):
        response = client.get("/items/1234")
        assert response.status_code == 200
        assert response.json() == {
            "item_id": 1234,
            "q": None,
        }

    def test_read_item_with_integer_id_and_querystring(self):
        response = client.get("/items/1234?q=hello")
        assert response.status_code == 200
        assert response.json() == {
            "item_id": 1234,
            "q": "hello",
        }

    def test_read_item_with_string_id(self):
        response = client.get("/items/hello")
        assert response.status_code == 422
        assert response.json() == {
            "detail": [
                {
                    "input": "hello",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                }
            ]
        }


@pytest.mark.api
class TestPut:
    def test_update_item_successfully_without_is_offer(self):
        response = client.put("/items/1234", json={"name": "book", "price": 10.0})
        assert response.status_code == 200
        assert response.json() == {
            "name": "book",
            "id": 1234,
            "price": 10.0,
            "is_offer": False,
        }

    def test_update_item_successfully_with_is_offer(self):
        response = client.put(
            "/items/6543", json={"name": "book", "price": 10.0, "is_offer": True}
        )
        assert response.status_code == 200
        assert response.json() == {
            "name": "book",
            "id": 6543,
            "price": 10.0,
            "is_offer": True,
        }

    def test_fail_to_update_item_with_string_id(self):
        response = client.put("/items/book", json={"name": "book", "price": 10.0})
        assert response.status_code == 422
        assert response.json() == {
            "detail": [
                {
                    "input": "book",
                    "loc": ["path", "item_id"],
                    "msg": "Input should be a valid integer, unable to parse string "
                    "as an integer",
                    "type": "int_parsing",
                }
            ]
        }

    def test_fail_to_update_item_with_missing_parameters(self):
        response = client.put("/items/987", json={})
        assert response.status_code == 422
        assert response.json() == {
            "detail": [
                {
                    "input": {},
                    "loc": ["body", "name"],
                    "msg": "Field required",
                    "type": "missing",
                },
                {
                    "input": {},
                    "loc": ["body", "price"],
                    "msg": "Field required",
                    "type": "missing",
                },
            ]
        }

import pytest

from main import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)

    with app.test_client() as client:
        yield client


def test_hello_returns_expected_message(client):
    response = client.get("/hello")

    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello world!"}


def test_calc_requires_an_expression(client):
    response = client.post("/calc", json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "expression is required"}


def test_calc_requires_json_body(client):
    response = client.post("/calc")

    assert response.status_code == 400
    assert response.get_json() == {"error": "expression is required"}


def test_calc_evaluates_expression(client):
    response = client.post("/calc", json={"expression": "2 * (3 + 4)"})

    assert response.status_code == 200
    assert response.get_json() == {
        "expression": "2 * (3 + 4)",
        "result": "14",
    }

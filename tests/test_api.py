import pytest

from main import app


# creating flask test client 
@pytest.fixture
def client(): 
    app.config.update({"TESTING": True})
    with app.test_client() as test_client:
        yield test_client


# 1. Verify the GET /hello route returns status 200 and the expected JSON payload.
def test_hello_endpoint(client):
    res = client.get("/hello")
    assert res.status_code == 200
    assert res.is_json
    assert res.get_json() == {"message": "Hello world!"}


# 2. Verify the POST /calc route correctly computes and formats a valid
# expression payload.
def test_calc_success(client):
    res = client.post("/calc", json={"expression": "10 * (2 + 3)"})
    assert res.status_code == 200
    assert res.is_json

    data = res.get_json()
    assert data["expression"] == "10 * (2 + 3)"
    assert data["result"] == "50"


# 2. Verify the POST /calc route returns HTTP 400 when the expression is missing.
@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"wrong_key": "3 + 5"},
    ],
)
def test_calc_missing_expression_key(client, payload):
    res = client.post("/calc", json=payload)
    assert res.status_code == 400
    assert res.get_json() == {"error": "expression is required"}


# 3. Verify the POST /calc route rejects non-JSON payloads with HTTP 400.
def test_calc_non_json_body(client):
    res = client.post(
        "/calc",
        data="expression=3+5",
        content_type="application/x-www-form-urlencoded",
    )
    assert res.status_code == 400
    assert res.get_json() == {"error": "expression is required"}


# 4. Document that unhandled calculator ValueError exceptions propagate
# through Flask during testing.
@pytest.mark.parametrize("invalid_expr", ["3 + a", "open('file')", "10 / 0"])
def test_calc_unhandled_calculator_error_bubbles_exception(client, invalid_expr):
    with pytest.raises(ValueError):
        client.post("/calc", json={"expression": invalid_expr})

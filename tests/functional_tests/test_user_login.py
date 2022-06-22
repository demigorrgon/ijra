import json


def test_user_login(api_client):
    response = api_client.post(
        "/api/v1/login",
        data=json.dumps({"username": "demitest", "password": "somepass1"}),
        content_type="application/json",
    )
    assert response.status_code == 200

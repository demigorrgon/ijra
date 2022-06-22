import json
from ijra import db


def test_get_categories(api_client):
    r = api_client.get("/api/v1/categories")
    assert r.status_code == 200


def test_create_category(api_client):
    payload = {"name": "wasda", "owner": "demitest"}
    response = api_client.post(
        "/api/v1/categories", data=json.dumps(payload), content_type="application/json"
    )
    db.session.rollback()
    assert response.status_code == 201

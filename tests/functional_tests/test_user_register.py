import json
from ijra import db


def test_user_can_register(api_client):
    response = api_client.post(
        "/api/v1/register",
        data=json.dumps({"username": "some", "password": "somepass"}),
        content_type="application/json",
    )
    db.session.rollback()
    # not unique
    assert response.status_code == 403

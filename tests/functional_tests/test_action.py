import json


def test_get_actions(api_client):
    response = api_client.get("/api/v1/actions")
    assert response.status_code == 200


def test_user_can_add_action(api_client):
    response = api_client.post(
        "/api/v1/actions",
        data=json.dumps(
            {
                "title": "New Cool title2",
                "description": "lorem inpum",
                "category_id": 3,
                "created_by": "demitest",
            },
        ),
        content_type="application/json",
    )
    return response.status_code == 201


def test_user_can_edit_action_by_action_name(api_client):
    response = api_client.put(
        "/api/v1/actions?action_name=New%20Cool%20title2",
        data=json.dumps(
            {
                "title": "New Cool title edit2",
                "description": "lorem inpum2",
                "category_id": 2,
                "created_by": "demitest",
            },
        ),
        content_type="application/json",
    )
    print(response.data)
    assert response.status_code == 200


def test_user_can_delete_action_by_action_name(api_client):
    response = api_client.delete(
        "/api/v1/actions?action_name=New%20Cool%20title%20edit2",
        content_type="application/json",
    )
    assert response.status_code == 200

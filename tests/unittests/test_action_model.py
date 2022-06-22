from ijra.models import ToDoAction


def test_create_action(dummy_user, dummy_category):
    action = ToDoAction(
        title="some action",
        description="lorem ipsum",
        category_id=dummy_category.id,
        created_by=dummy_user.username,
    )
    assert action.created_by == dummy_user.username

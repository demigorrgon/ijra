from ijra.models import Category


def test_create_category(dummy_user):
    category = Category(name="wasda", owner=dummy_user)
    assert category.owner.username == dummy_user.username

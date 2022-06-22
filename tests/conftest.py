import pytest

from ijra import create_app
from ijra.models import AuthUser, Category


@pytest.fixture
def dummy_user():
    user = AuthUser(username="dumm", password="somepass")
    return user


@pytest.fixture
def dummy_category():
    category = Category(name="candies", owner=dummy_user)
    return category


@pytest.fixture(scope="module")
# TODO: find a way to create temporary test db (like in django)
def api_client():
    app = create_app()
    with app.test_client() as test_client:
        with app.app_context():
            yield test_client

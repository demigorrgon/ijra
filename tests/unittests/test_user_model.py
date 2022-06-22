def test_is_user_created(dummy_user):
    assert dummy_user.username is not None
    assert dummy_user.username == "dumm"


def test_is_password_hashed(dummy_user):
    assert dummy_user.check_password("somepass") is True

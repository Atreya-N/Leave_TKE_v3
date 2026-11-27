from werkzeug.security import check_password_hash

from app.repositories.user_repository import get_user_by_username


def authenticate_user(username, password):
    """
    Authenticate a user using their username and password.

    Returns:
        User object if authentication succeeds.
        None if authentication fails.
    """

    user = get_user_by_username(username)

    if user is None:
        return None

    if not check_password_hash(user.password_hash, password):
        return None

    return user
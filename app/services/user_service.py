
from werkzeug.security import generate_password_hash

from app.models import User
from app.repositories.user_repository import (
    get_user_by_username,
    get_user_by_id,
    add_user
)


ALLOWED_ROLES = [
    "employee",
    "manager",
    "admin",
    "super_admin"
]


def create_user(username, password, role, manager_id=None):
    """
    Validate and create a new user.

    Raises:
        ValueError: If the supplied user information is invalid.

    Returns:
        The newly created User object.
    """

    # Validate required fields
    if not username or not password or not role:
        raise ValueError("All required fields must be filled!")

    # Validate role
    if role not in ALLOWED_ROLES:
        raise ValueError("Invalid user role selected!")

    # Check duplicate username
    existing_user = get_user_by_username(username)

    if existing_user:
        raise ValueError("This username already exists!")

    # Validate manager assignment
    assigned_manager = None

    if role == "employee" and manager_id:

        try:
            manager_id = int(manager_id)
        except (TypeError, ValueError):
            raise ValueError("Invalid manager selected!")

        assigned_manager = get_user_by_id(manager_id)

        if assigned_manager is None or assigned_manager.role != "manager":
            raise ValueError("Selected manager does not exist!")

    # Hash password
    hashed_password = generate_password_hash(password)

    # Create user object
    new_user = User(
        username=username,
        password_hash=hashed_password,
        role=role,
        manager_id=assigned_manager.id if assigned_manager else None
    )

    # Save user
    add_user(new_user)

    return new_user

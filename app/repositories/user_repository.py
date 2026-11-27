from app.database import db
from app.models import User


def get_user_by_username(username):
    return User.query.filter_by(username=username).first()


def get_user_by_id(user_id):
    return db.session.get(User, user_id)


def get_all_users():
    return User.query.order_by(User.id.desc()).all()


def get_users_by_manager(manager_id):
    return User.query.filter_by(manager_id=manager_id).all()


def get_all_managers():
    return User.query.filter_by(role="manager").all()


def add_user(user):
    db.session.add(user)
    db.session.commit()
    return user
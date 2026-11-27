from app.database import db


class User(db.Model):
    __tablename__ = "Users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(20), nullable=False, default="employee")

    manager_id = db.Column(
        db.Integer,
        db.ForeignKey("Users.id"),
        nullable=True
    )
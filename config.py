import os

class Config:
    # Application security
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only")

    # Database configuration
    SQLALCHEMY_DATABASE_URI = "sqlite:///leave_db.db"

    # Disable unnecessary SQLAlchemy event tracking
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Application debugging
    DEBUG = os.environ.get("FLASK_DEBUG") == "1"x

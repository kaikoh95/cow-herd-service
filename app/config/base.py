import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    """
    Base application configuration
    """
    PROJECT_NAME = os.getenv("PROJECT_NAME")
    DEBUG = os.getenv("DEBUG", False)
    TESTING = os.getenv("TESTING", False)
    
    ENV = os.getenv("ENV")
    FLASK_ENV = os.getenv("FLASK_ENV")
    
    HALTER_API = os.getenv("HALTER_API")

    DB_NAME = os.getenv("DB_NAME")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_PORT = os.getenv("DB_PORT")

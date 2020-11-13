import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "duck"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = "postgresql+psycopg2://app:testing@localhost:5432/library_api"

        if not value:
            raise ValueError("DB_URI is not set")

        return value

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.getenv("JWT_SECRET_KEY")
        
        if not value:
            raise ValueError("JWT_SECRET_KEY is not set")
        
        return value

class TestingConfig(Config):
    TESTING = True

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()
"""
    Configuration
    _______________
    This is module for storing all configuration for various environments
"""
import os

basedir = os.path.abspath(os.path.dirname("data"))

class Config:
    """ This is base class for configuration """
    # DEBUG = False
    JSON_SORT_KEYS = False
    
    DATABASE = {
        "DRIVER"   : os.getenv('DB_DRIVER') or "postgresql://", # sqlite // postgresql // mysql
        "USERNAME" : os.getenv('DB_USERNAME') or "fajar",
        "PASSWORD" : os.getenv('DB_PASSWORD') or "cangcimen",
        "HOST_NAME": os.getenv('DB_HOSTNAME') or "localhost",
        "DB_NAME"  : os.getenv('DB_NAME') or "db_era",
        "PORT"  : os.getenv('DB_PORT') or '5432',
    }

    SENTRY_CONFIG = {}

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False

#end class


class DevelopmentConfig(Config):
    """ This is class for development configuration """
    DEBUG = True

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + ":" + DATABASE["PORT"] + "/" + \
            DATABASE["DB_NAME"] + "_dev"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    # SQLALCHEMY_ECHO = True
#end class


class TestingConfig(Config):
    """ This is class for testing configuration """
    DEBUG = True
    TESTING = True

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + ":" + DATABASE["PORT"] +  "/" + \
            DATABASE["DB_NAME"] + "_testing"

    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
#end class


class ProductionConfig(Config):
    """ This is class for production configuration """
    DEBUG = False

    DATABASE = Config.DATABASE
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
            DATABASE["DRIVER"] + DATABASE["USERNAME"] + ":" + \
            DATABASE["PASSWORD"] + "@" + DATABASE["HOST_NAME"] + ":" + DATABASE["PORT"] +  "/" + \
            DATABASE["DB_NAME"] + "_prod"
    PRESERVE_CONTEXT_ON_EXCEPTION = False                         
#end class

CONFIG_BY_NAME = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)
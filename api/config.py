import os

class DevelopmentConfig:

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@db/test_database?charset=utf8".format(
        **{
            "user": os.getenv("DB_USER", "root"),
            "password": os.getenv("DB_PASSWORD", "root"),
            "host": os.getenv("DB_HOST", "db"),
            "database": os.getenv("DB_DATABASE", "test_database")
         })

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig


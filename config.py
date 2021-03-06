import os
class Config:
    """
    Main configurations class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wanjiru:BlackSheep2016@localhost/bchic'
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY ='black2345'
    UPLOADED_PHOTOS_DEST='app/static/images'
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class DevConfig(Config):
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    # 'test':TestConfig
}

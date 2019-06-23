import os

class Config:
    SECRET_KEY = 'b06af82bdbb223bb5f91a4300f173437'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # for use with email verification
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

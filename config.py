import os

class Config(object):
    DEBUG = True
    CSRF_ENABLED = True
    #SECRET_KEY = os.environ.get('SECRET_KEY') or 'neotchislyaitemenyapozhaluista'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///forum.bd'

    ################
    # Flask-Security
    ################

    SECURITY_PASSWORD_HASH = "pbkdf2_sha512"
    SECURITY_PASSWORD_SALT = "fsdfdfsdfdfsdafds"

class Config:
    SECRET_KEY = '1234567890'

class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask_login'

config = {
    'development': DevelopmentConfig
}
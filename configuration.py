class Config(object):
    'Configuracion basica'
    SECRET_KEY = 'Key'
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@127.0.0.1:5432/papeleria2'
    #SQLALCHEMY_DATABASE_URI='postgresql://postgres:1234@127.0.0.1:5432/papeleria2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProduccionConfig(Config):
    'Configurtacion produccion'
    DEBUG = True


class DevelopmentConfig(Config):
    'Configuracion de desarrollo'
    DEBUG = True
    TESTING = True
    SECREY_KEY = 'tienda'

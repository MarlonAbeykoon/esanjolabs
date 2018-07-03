import tempfile


class TestingConfig():
    """ Sets config for testing """
    TESTING = True
    DB_FD, DATABASE = tempfile.mkstemp()
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:DuoS123@localhost/esanjo'
    SECRET_KEY = 'esanjolabssecret'

#  This can be extended to have several configs eg: dev, production

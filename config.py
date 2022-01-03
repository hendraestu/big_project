import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    HOST = "localhost"
    DATABASE = "bigpro"
    USERNAME = "root"
    PASSWORD = "hendra24"
    JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
    #SQLALCHEMY_DATABASE_URI = 'mysql://'+USERNAME+':'+PASSWORD+'@'+HOST+'/'+DATABASE
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:hendra24@localhost/bigpro'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_RECORD_QUERIES = True
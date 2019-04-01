from pymongo import MongoClient

class Config(object):
    DB_CLIENT = MongoClient(
        'localhost',
        port=27017,
        username='username',
        password='password',
        authSource='authentication database',
        authMechanism='SCRAM-SHA-256'
    )

    DB = DB_CLIENT['database']
    SC = DB['collection']
from peewee import *
from configparser import ConfigParser

conf = ConfigParser()
conf.read("config.ini")
userName=conf.get('Database', 'uName')
password=conf.get('Database', 'pwd')
hostName=conf.get('Database', 'host')
port=conf.getint('Database', 'port')

db = MySQLDatabase('cardb',host=hostName,
        port=port,
        user=userName,
        passwd=password
        )

class UserCredentials(Model):
    userName = CharField()
    password = CharField()
    emailID = CharField(primary_key=True)
    class Meta:
        database = db # This model uses the "people.db" database.

def putUserDetails():
    pass
    # TODO: complete function
    db.connect()
   # UserCredentials.create(userName=)


def getUserPassword(userName):

    db.connect()
    user=UserCredentials.get(UserCredentials.userName == userName)
    db.close()

    return user.password
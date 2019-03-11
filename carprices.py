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

class carprices(Model):
    Car_Company = CharField()
    Car_Name = CharField()
    Car_Price=IntegerField(primary_key=True)
    Car_Variant= CharField()
    class Meta:
        database = db # This model uses the "people.db" database.


def getCarNames(carCompany):
    db.connect()

    query = carprices.select(carprices.Car_Name).distinct().where(carprices.Car_Company == carCompany)
    return [user.Car_Name for user in query]

    db.close()

def getCarVariants(carCompany,carName):
    db.connect()

    query = carprices.select(carprices.Car_Variant).distinct().where(carprices.Car_Company == carCompany & carprices.Car_Company == carName)
    return [user.Car_Name for user in query]

    db.close()
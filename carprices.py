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
    db.close()
    return [user.Car_Name for user in query]



def getCarVariants(carCompany,carName):

    db.connect()
    query = carprices.select(carprices.Car_Variant)\
        .distinct()\
        .where((carprices.Car_Name == carName) & (carprices.Car_Company == carCompany))
    db.close()
    return [user.Car_Variant for user in query]

def getcarPrice(carParam):

    db.connect()
    query = carprices.select(carprices.Car_Price)\
        .where((carprices.Car_Name == carParam["carName"])\
               & (carprices.Car_Company == carParam["carMake"])\
               & (carprices.Car_Variant == carParam["carVariant"]))
    db.close()
    x=[user.Car_Price for user in query]
    return x[0]
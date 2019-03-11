from flask import Flask,render_template,request
import pymysql
from configparser import ConfigParser
from flask import jsonify
import carprices

conf = ConfigParser()
conf.read("config.ini")
userName=conf.get('Database', 'uName')
password=conf.get('Database', 'pwd')
hostName=conf.get('Database', 'host')
port=conf.getint('Database', 'port')

def getcarDBdata(carParam):
    mydb = pymysql.connect(
        host=hostName,
        port=port,
        user=userName,
        passwd=password,
        db='cardb'
    )

    mycursor = mydb.cursor()
    #carParam = ("Maruti Suzuki", "S Cross", "Zeta 1.3 Le")

    dataQuery = "select Car_Price from  carprices where Car_Company=%s and Car_Name=%s and Car_Variant=%s"

    mycursor.execute(dataQuery, carParam)

    mydb.close()

    myresult = mycursor.fetchone()

    return myresult


def getcarModels(Car_Company):

    mydb = pymysql.connect(
        host=hostName,
        port=port,
        user=userName,
        passwd=password,
        db='cardb'
    )

    dataQuery = "select distinct Car_Name from  carprices where Car_Company=%s"

    mycursor = mydb.cursor()

    mycursor.execute(dataQuery, Car_Company)

    mydb.close()

    carModels = mycursor.fetchall()

    return {Car_Company:carModels}

def carPriceFormula(basePrice):
    carCondition={"Poor":basePrice*.75,"Good":basePrice*.85,"Excellent":basePrice*.95}
    return carCondition


app = Flask(__name__,template_folder='template')

@app.route('/')
def test_route():
    user_details = {
        'name': 'John',
        'email': 'john@doe.com'
    }
    request.form.get("")

    return render_template('home.html')

@app.route('/carPrice', methods=['GET', 'POST'])
def index():
    carMake = request.args.get("car_make")
    carName = request.args.get("car_name")
    carVariant = request.args.get("car_variant")

    carParam = (carMake, carName, carVariant)

    price = getcarDBdata(carParam)

    carParam = {"carMake": carMake, "carName": carName, "carVariant": carVariant}



    if price != None:
        carPrices = carPriceFormula(price[0])
        return render_template('test.html', carPrice=carPrices,carParam=carParam)
    return render_template('carnotFound.html',  carParam=carParam)

@app.route('/background_process')
def background_process():
    #lang = request.args.get('proglang', 0, type=str)
    lan = request.args.get('carCompany', 0, type=str)
    carModels=carprices.getCarNames(lan)
    print(carModels)
    return jsonify(result=carModels)


@app.route('/back')
def back():
    return render_template('dynamicRender.html')

if __name__ == '__main__':
    app.run(debug=True)

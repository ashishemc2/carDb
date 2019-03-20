from flask import Flask,render_template,request
import pymysql
from configparser import ConfigParser
from flask import jsonify
import carprices
from UserValidations import Credentials

conf = ConfigParser()
conf.read("config.ini")
userName=conf.get('Database', 'uName')
password=conf.get('Database', 'pwd')
hostName=conf.get('Database', 'host')
port=conf.getint('Database', 'port')

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

    #carParam = (carMake, carName, carVariant)

    carParam = {"carMake": carMake, "carName": carName, "carVariant": carVariant}

    price = carprices.getcarPrice(carParam)

    if price != None:
        carPrices = carPriceFormula(price)
        return render_template('test.html', carPrice=carPrices,carParam=carParam)
    return render_template('carnotFound.html',  carParam=carParam)

@app.route('/background_process')
def background_process():
    #lang = request.args.get('proglang', 0, type=str)
    carCompany = request.args.get('carCompany', 0, type=str)
    carName = request.args.get('carName', 0, type=str)

    carDetails=[]
    if (carCompany and carName):
        carVariants =carprices.getCarVariants(carCompany,carName)
        carDetails=carVariants
    elif (carCompany):
        carNames = carprices.getCarNames(carCompany)
        carDetails=carNames
    return jsonify(result=carDetails)


@app.route('/back')
def back():
    return render_template('dynamicRender.html')

@app.route('/login')
def login():
    return render_template('loginPage.html')

@app.route('/account',methods=['POST'])
def account():
    userName = request.form.get('uname', 0, type=str)
    password = request.args.get('psw', 0, type=str)
    userCred=Credentials(userName,password)
    userCred.verifyUser()

    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')

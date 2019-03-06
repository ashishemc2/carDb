from flask import Flask,render_template,request
from pymysql 


def getDBdata(carParam):
    mydb = pymysql.connect(
        host="127.0.0.1",
        port=5432
        user="proxyuser",
        passwd="potihari1"
    )

    mycursor = mydb.cursor(buffered=True)

    mycursor.execute("SHOW DATABASES")

    mycursor.execute("use cardb")

    mycursor.execute("show tables")

    #carParam = ("Maruti Suzuki", "S Cross", "Zeta 1.3 Le")

    dataQuery = "select Car_Price from  carprices where Car_Company=%s and Car_Name=%s and Car_Variant=%s"

    mycursor.execute(dataQuery, carParam)

    myresult = mycursor.fetchone()

    return myresult

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

    price = getDBdata(carParam)

    carParam = {"carMake": carMake, "carName": carName, "carVariant": carVariant}



    if price != None:
        carPrices = carPriceFormula(price[0])
        return render_template('test.html', carPrice=carPrices,carParam=carParam)
    return render_template('carnotFound.html',  carParam=carParam)

if __name__ == '__main__':
   app.run()

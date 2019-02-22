import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)

mycursor = mydb.cursor(buffered=True)



mycursor.execute("SHOW DATABASES")



mycursor.execute("use cardb")

mycursor.execute("show tables")


carParam=("Maruti Suzuki","S Cross","Zeta 1.3 Le")
dataQuery="select Car_Price from  carprices where Car_Company=%s and Car_Name=%s and Car_Variant=%s"

mycursor.execute(dataQuery,carParam)

myresult = mycursor.fetchone()

print( myresult)

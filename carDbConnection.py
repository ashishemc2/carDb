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

mycursor.execute("select * from carprices")

myresult = mycursor.fetchall()

print( myresult)

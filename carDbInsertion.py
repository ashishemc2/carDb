import mysql.connector
import csv




def getDatafromCsv(fileName):

    with open(fileName) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)


data=getDatafromCsv("D:\\Vaibhav\\cardetails.txt")


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)
mycursor = mydb.cursor(buffered=True)

mycursor.execute("SHOW DATABASES")
mycursor.execute("use cardb")




for i in range(len(data)):

    if data[i][3].isdigit():
        data[i][3]=int(data[i][3])
    else :
        data[i][3]=0
    data[i]=tuple(data[i])
#data=('Maruti Suzuki', '1000','AC',27342)

print(data)

sql = "INSERT INTO carprices (Car_Company, Car_Name,Car_Variant,Car_Price) VALUES (%s, %s,%s,%s)"

for i in data:
    try:
        mycursor.execute(sql,i)
    except:
        print(i)
mydb.commit()

#print( myresult)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="7Al@wiyat"
)

mycursor = mydb.cursor()

print(mydb.get_server_info())

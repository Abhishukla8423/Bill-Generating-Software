import mysql.connector
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Shukla@123",
)
c=mydb.cursor()
c.execute("CREATE DATABASE shop")
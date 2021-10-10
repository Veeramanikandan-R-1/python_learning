import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="Mani123#"
)
#print(mydb)
cursor=mydb.cursor()
cursor.execute("CREATE DATABASE college_db;")

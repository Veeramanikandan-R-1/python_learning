import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="Mani123#",
database='college_details'
)
#print(mydb)
cursor=mydb.cursor()
cursor.execute('CREATE TABLE degree_table(degree_id int not null AUTO_INCREMENT,degree_name varchar(25) not null,PRIMARY KEY(degree_id));')
cursor.execute("SHOW CREATE TABLE degree_table")
for db in cursor:
	print(db)

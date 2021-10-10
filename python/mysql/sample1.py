import mysql.connector
class store_db:
	def __init__(self,db_name):
		self.db_name=db_name
	def db_connect(self):
		mydb=mysql.connector.connect(
		host="localhost",
		user="root",
		password="Mani123#",
		database="college_details")
		
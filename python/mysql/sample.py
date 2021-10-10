import mysql.connector
mydb=mysql.connector.connect(
host="localhost",
user="root",
password="Mani123#",
database="college_details"
)
#print(mydb)
cursor=mydb.cursor()
def update_sale_tb():
	cursor.execute("update sale_tb set price_per_unit=(select product_price_per_unit from product_tb where sale_tb.product_id=product_tb.product_id);")
	cursor.execute("update sale_tb set total_price=no_of_units*price_per_unit;")
	mydb.commit()
def insert_fun(query,value_list):
	print(value_list)
	cursor.execute(query,value_list)
	mydb.commit()
	update_sale_tb()
	
	
insert_fun("INSERT INTO sale_tb(customer_id,product_id,sale_date,no_of_units) values(%s,%s,%s,%s);",(2,2,'2021-10-8',6))
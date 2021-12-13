import re
import traceback
import mysql.connector

import logging
logging.basicConfig(level=logging.DEBUG,filename='sample.log',filemode='a',format='%(asctime)s - %(process)d - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

mydb=mysql.connector.connect(
host="localhost",
user="root",
password="Mani123#",
database="college_details"
)

cursor=mydb.cursor()

logger=logging.getLogger(__name__)

def fetching_products():
	try:
		cursor.execute("select product_name from product_tb;")
		existing_products=[x[0] for x in cursor.fetchall()]
		return existing_products
	except Exception as error:
		# print("error occured\n")
		# print(traceback.format_exc())
		logger.error(traceback.format_exc())

def fetching_customer():
	try:
		cursor.execute("select name from customer_tb;")
		existing_user=[x[0] for x in cursor.fetchall()]
		cursor.execute("select phone_no from customer_tb;")
		existing_user_phone_no=[x[0] for x in cursor.fetchall()]
		#print(existing_user)
		#print(existing_user_phone_no)
		return existing_user,existing_user_phone_no
	except Exception as error:
		# print("error occured\n",error)
		# print(traceback.format_exc())
		logger.error(traceback.format_exc())

def add_customer():
	try:
		name=input('enter name')

		while True:
			phone_no=int(input('enter mobile number'))
			check=re.findall("(0|91)?[7-9][0-9]{9}",str(phone_no))
			if check:
				break
			else:
				print('enter valid phone no')

		age=int(input(('enter age')))
		gender=input('enter sex M/F')

		query_to_add="insert into customer_tb(name,phone_no,age,gender) values(%s,%s,%s,%s);"
		user_details=(name,phone_no,age,gender)
		existing_user,existing_user_phone_no=fetching_customer()
		#print(existing_user)
		#print(existing_user_phone_no)
		#print(fetching_customer())
		if(name not in existing_user):
			cursor.execute(query_to_add,user_details)
			mydb.commit()
			if name in existing_user:
				print("customer added successfully")

		elif(name in existing_user and phone_no!=existing_user_phone_no[existing_user.index(name)]):
			# print(existing_user_phone_no[existing_user.index(name)])
			cursor.execute(query_to_add,user_details)
			mydb.commit()
			#print(fetching_customer())
			if name in existing_user:
				print("customer added successfully")
		else:
			return print('already existing user try with different name/mobile number')
		return name
	except Exception as error:
		# print("error occured\n",error)
		# print(traceback.format_exc())
		logger.error(traceback.format_exc())

def adding_product():
	try:
		pro_name=input('enter product name')
		price_per_unit=int(input('enter price per unit'))
		no_of_stocks=int(input('enter no of stocks'))
		category=input('enter product category')

		query_to_add="insert into product_tb(product_name,product_price_per_unit,no_of_stocks,category) values(%s,%s,%s,%s);"
		product_details=(pro_name,price_per_unit,no_of_stocks,category)

		#print(fetching_products())
		if(pro_name not in fetching_products()):
			cursor.execute(query_to_add,product_details)
			mydb.commit()
			#print(fetching_customer())
			if pro_name in fetching_products():
				print("product added successfully")
		else:
			return print('product already exists')

	except Exception as error:
		# print("error occured\n",error)
		# print(traceback.format_exc())
		logger.error(traceback.format_exc())

def sale_fun():
	try:
		customer_name=input('enter name')
		existing_user,existing_user_phone_no=fetching_customer()

		if(customer_name not in existing_user): #to check customer exists
			print("invalid customer")
			customer_name=add_customer()



		# to find sales id
		cursor.execute('select count(distinct(bill_id)) from sale_tb')

		bill_id=(cursor.fetchone())[0]+1
		# print(bill_id)

		add_product_list = []

	except Exception as error:
		logger.error(traceback.format_exc())

		def add_product():
			try:
				cursor.execute("select product_name from product_tb where no_of_stocks>0;")
				existing_products = [x[0] for x in cursor.fetchall()]
				print(existing_products)
				product_name=input('select products from the list')
				add_product_list.append(product_name)
				no_of_units=int(input('enter no of units'))
				cursor.execute("select product_id,no_of_stocks from product_tb where product_name=%s",(product_name,))
				result=cursor.fetchone()

				if(result[1]<=0): #to check no of stocks in product table
					return print("selected product out of stock")

				cursor.execute("select name from customer_tb;")
				customer_list=[x[0] for x in cursor.fetchall()]
				#print(customer_list)
				if customer_name in customer_list:
					cursor.execute("select customer_id from customer_tb where name=%s",(customer_name,))
					customer_id=(cursor.fetchall())[0][0]

					cursor.execute("select product_id from product_tb where product_name=%s",(product_name,))
					product_id=(cursor.fetchall())[0][0]

					query_to_add="insert into sale_tb(bill_id,customer_id,product_id,no_of_units) values(%s,%s,%s,%s);"
					sale_details=(bill_id,customer_id,product_id,no_of_units)
					cursor.execute(query_to_add,sale_details)
					mydb.commit()

					# cursor.execute("update sale_tb set price_per_unit=(select product_price_per_unit from product_tb where sale_tb.product_id=product_tb.product_id);")
					cursor.execute("select product_price_per_unit from product_tb where product_id=%s",(result[0],))
					price_per_unit=cursor.fetchall()[0][0]
					cursor.execute("update sale_tb set total_price=no_of_units*%s;",(price_per_unit,))
					mydb.commit()
					cursor.execute('select no_of_stocks from product_tb where product_id=%s',(product_id,))
					stock_count=(cursor.fetchall())[0][0]
					cursor.execute('update product_tb set no_of_stocks=%s where product_id=%s',(stock_count-no_of_units,product_id))
					mydb.commit()

				else:
					print('customer not found add in customer details')
			except Exception as error:
				print("error occured\n", error)
				print(traceback.format_exc())

		def billing():
			try:
				# query = 'select sale_date,no_of_units,price_per_unit,total_price from sale_tb where bill_id=%s'
				query = 'select sale_date,no_of_units,product_tb.product_price_per_unit,total_price from sale_tb inner join product_tb on product_tb.product_id=sale_tb.product_id where bill_id=%s'
				value = (bill_id,)
				cursor.execute(query,value)
				bill_details=cursor.fetchall()
				loop_length=len(bill_details)
				print('************---bill---***************')
				print('customer name:{}'.format(customer_name))
				print('bill_id: {} ---------date: {}'.format(bill_id,bill_details[0][0]))
				# print(bill_details)
				ind = 1
				total_amount=0
				for val in bill_details:
					print('{}. {} ------ {} * {} = {:.2f}'.format(ind,add_product_list[ind-1],val[1],val[2],val[3]))
					total_amount+=val[3]
					ind+=1
				print("Total amount ------------ Rs.{:.2f}".format(total_amount))
				print("GST amount -------------- Rs.{:.2f}".format(total_amount*0.18))
				print("Total amount ------------ Rs.{:.2f}".format(total_amount+(total_amount*0.18)))
				print('*******---Thank you visit again---******')
			except Exception as error:
				print("error occured\n", error)
				print(traceback.format_exc())


		while True:
			choice=int(input('enter choice 1 to add product\t2 for billing'))
			if(choice==1):
				add_product()
			elif(choice==2):
				return billing()



	except Exception as error:
		print("error occured\n",error)
		print(traceback.format_exc())

def daily_turn_over(): #to get daily turn over based on date
	try:
		date_inp=input("enter date in YY-MM-DD format")
		date_inp_m="%"+date_inp+"%"
		query='select sum(total_price) from sale_tb where sale_date like %s'
		cursor.execute(query,(date_inp_m,))
		print('daily turn over for the date {} is {}'.format(date_inp,(cursor.fetchone())[0]))
		gender_choice=input('enter M/F')
		query = 'select distinct(customer_id) from sale_tb where sale_date like %s;'
		cursor.execute(query, (date_inp_m,))
		customer_list=[x[0] for x in cursor.fetchall()]
		daily_customers=[]

		for id in customer_list:
			query = 'select name from customer_tb where ((customer_id=%s)and (gender=%s));'
			value=(id,gender_choice)
			cursor.execute(query,value)
			name=cursor.fetchone()
			if name:
				daily_customers.append(name[0])
		# print(daily_customers)
		if daily_customers:
			print("no of {} customers on {} is {} \n {}".format(gender_choice,date_inp,len(daily_customers),daily_customers))
		else:
			print('NO {} customers on {}'.format(gender_choice,date_inp))
	except Exception as error:
		print("error occured\n",error)
		print(traceback.format_exc())


def total_revenue(): #to get total revenue till date
	try:
		cursor.execute('select sum(total_price) from sale_tb')
		print('total revenue_till date is {}'.format(((cursor.fetchone())[0])))
	except Exception as error:
		print("error occured\n",error)
		print(traceback.format_exc())

def frequent_buyer_fun():
	try:
		# cursor.execute("select name,no_of_purchases from customer_tb order by no_of_purchases desc;")
		cursor.execute("select distinct(customer_id) from sale_tb")
		distinct_customers=[x[0] for x in cursor.fetchall()]
		# print(distinct_customers)
		frequent_buyer={}
		for val in distinct_customers:
			cursor.execute("select name from customer_tb where customer_id=%s;",(val,))
			cus_name = cursor.fetchone()[0]
			cursor.execute("select count(distinct(bill_id)) from sale_tb where customer_id=%s;",(val,))
			details=cursor.fetchone()[0]
			frequent_buyer[cus_name]=details
		# print(frequent_buyer)
		sorted_dic=sorted(frequent_buyer.items(),key=lambda x:x[1])
		print(sorted_dic)
			# for x in range(len(details)):
			# 	print("rank:{} customer name:{} total_purchases:{}".format(x+1,details[x][0],details[x][1]))
	except Exception as error:
		print("error occured\n",error)
		print(traceback.format_exc())

def update_product_stocks():
	try:
		print(fetching_products())
		product_name=input("choose product from above list")
		no_of_units=int(input('enter no of stocks to add'))
		cursor.execute('select no_of_stocks from product_tb where product_name=%s', (product_name,))
		stock_count = (cursor.fetchone())[0]
		cursor.execute('update product_tb set no_of_stocks=%s where product_name=%s', (stock_count + no_of_units, product_name))
		mydb.commit()
	except Exception:
		print("error occured\n",error)
		print(traceback.format_exc())

while True:
	choice=int(input("Enter choice\n1 for user\n2 for admin\n"))
	if(choice==1):
		sale_fun()
	else:
		check=input('enter password\n')
		if(check=="admin"):
			print("admin actions")
			admin_choice=int(input('enter choices\n1.for adding customer\n2.for adding products\n3.for total revenue'
								   '\n4.to know frequent buyers\n5.to update product stocks\n6.for finding daily turnover\n7.to exit\n'))
			if(admin_choice==1):
				add_customer()
			elif(admin_choice==2):
				adding_product()
			elif(admin_choice==3):
				total_revenue()
			elif(admin_choice==4):
				frequent_buyer_fun()
			elif(admin_choice==5):
				update_product_stocks()
			elif (admin_choice == 6):
				daily_turn_over()
			elif (admin_choice == 7):
				break
			else:
				print('enter valid choice')
				mydb.close()

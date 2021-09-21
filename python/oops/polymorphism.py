#using same function call for multiple objects
class employee:
	def employee_type(self):
		print("full time")
	def employee_role(self):
		print("may be development or tester")
class developer(employee):
	def employee_role(self):
		print("developer")
class tester(employee):
	def employee_role(self):
		print('tester')
emp1=tester()
emp1.employee_type()
emp1.employee_role()

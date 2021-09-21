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
def fun(obj):
	obj.employee_type()
	obj.employee_role()
	

emp1=tester()
emp2=developer()

fun(emp1)
fun(emp2)

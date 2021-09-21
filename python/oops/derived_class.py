class cal1:
	def addition(self,a,b):
		return a+b
class cal2:
	def subtraction(self,a,b):
		return a-b
class cal3:
	def multiplication(self,a,b):
		return a*b
class derived(cal1,cal2,cal3):
	def divide(self,a,b):
		return a/b
d=derived()
print(d.addition(1,2))
print(d.subtraction(3,4))
print(d.multiplication(5,6))
print(d.divide(8,4))	

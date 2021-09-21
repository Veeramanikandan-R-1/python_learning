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
print(issubclass(derived,cal1))
print(issubclass(cal1,cal2))

print(isinstance(d,derived))
print(isinstance(d,cal1))

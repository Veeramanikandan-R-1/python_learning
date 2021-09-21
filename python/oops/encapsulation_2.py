class base:
	def __init__(self):
		self.a=2
		self.__b=3
class derived(base):
	def __init__(self):
		super().__init__()
		print(self.a)
		#print(self.__b)
obj1=base()
print(obj1.__b)
#obj2=base()
#print(obj2.a) #but can be accessed if we use _a


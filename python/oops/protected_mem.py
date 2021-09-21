class base:
	def __init__(self):
		self._a=2
class derived(base):
	def __init__(self):
		super().__init__()
		print(self._a)
obj1=derived()
obj2=base()
print(obj2.a) #but can be accessed if we use _a


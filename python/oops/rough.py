class Person:
	def __init__(self,age=0,name):
		self.name=name
		self.__age=age
	def display(self):
		print(self.name)
		print(self.__age)
person=Person(23,'mani')
person.display()
print(person.__age)

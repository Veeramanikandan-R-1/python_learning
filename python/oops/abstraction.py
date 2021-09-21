from abc import ABC,abstractmethod
class car(ABC):
	def mileage(self):
		pass
class tesla(car):
	def mileage(self):
		print('30')
class honda(car):
	def mileage(self):
		print('10')
t=tesla()
t.mileage()
h=honda()
h.mileage()

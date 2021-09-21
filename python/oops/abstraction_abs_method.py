import abc
from abc import ABC,abstractmethod
class animal(ABC):
	def man(self):
		pass
	@abstractmethod
	def speak(self):
		pass
class dog(animal):
	def speak(self):
		print("bark")
d=dog()
d.speak()

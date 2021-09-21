import abc
from abc import ABCMeta,abstractmethod
class shape:
	__metaclass__=ABCMeta
	def __init__(self,shapetype):
		self.shapetype=shapetype
	@abstractmethod
	def perimeter(self):
		pass
	@abstractmethod
	def area(self):
		pass
class rectangle(shape):
	def __init__(self,length,breadth):
		shape.__init__(self,'rectangle')
		self.length=length
		self.breadth=breadth
	def area(self):
		return self.length*self.breadth
rec=rectangle(4,5)
print(rec.area())

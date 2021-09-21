import abc
from abc import ABC, abstractmethod
class r(ABC):
	def rk(self):
		print('abs base class')
class k(r):
	def rk(self):
		super().rk()
		print('subclass')
a=k()
a.rk()
b=r()
b.rk()

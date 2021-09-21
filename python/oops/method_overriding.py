class animal:
	def speak(self):
		print("speaking")
class dog(animal):
	def speak(self):
		print("barking")
d=dog()
d.speak()

class animal:
	def speak(self):
		print('animal speaking')

class dog(animal):
	def bark(self):
		print("dog barks")
class dog_child(dog):
	def eating(self):
		print("eats meat")
d=dog_child()
d.speak()
d.bark()
d.eating()
		

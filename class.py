class Animal():
	def __init__(self,name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Subclass must implement this abstract method")


class Dog(Animal):
	def speak(self):
		return self.name


doggy1 = Dog('Frank')
doggy2 = Dog('Tom')

def pet_speak(pet):
	return pet.speak()

for pet in [doggy1,doggy2]:
	print(pet_speak(pet))

'''
class Line:

	def __init__(self, c1, c2):
		
		self.x1 = c1[0]
		self.y1 = c1[1]

		self.x2 = c2[0]
		self.y2 = c2[1]

	def distance(self):
		
		return ((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)**.5

	def slope(self):

		return (self.y2-self.y1)/(self.x2-self.x1)


coordinate1 = (3,2)
coordinate2 = (8,10)

li = Line(coordinate1, coordinate2)

print(li.distance())

print(li.slope())



class Cyclinder():

	def __init__(self, height, radius):

		self.pi = 3.14
		self.radius = radius
		self.height = height

	def volume(self):
		
		return self.pi * self.height * (self.radius)**2

	def surface(self):

		top = self.pi * (self.radius**2)

		return (2*top) + (2*3.14*self.radius*self.height)


c = Cyclinder(2,3)

print(c.volume())
print(c.surface())

'''


class Account:
	def __init__(self, owner, balance):
		self.owner = owner
		self.balance = balance

	def __str__(self):
		return "Account owner:   "+self.owner+'\n'+"Account balance: "+str(self.balance)


	def deposit(self, amount):
		return self.balance + amount
		print('Deposit Accepted')

	def withdrawl(self, amount):
		temp = self.balance - amount
		if temp < 0:
			return "Insufficient Funds"
		else:
			return temp

a = Account('John',300)

print(a)
print(a.owner)
print(a.balance)

print(a.deposit(100))
print(a.withdrawl(100))
print(a.withdrawl(900))
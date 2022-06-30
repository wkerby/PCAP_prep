#create a pet superclass, then create 'cat' and 'dog' subclasses
class Pet:
	def __init__(self):
		self.name = name
		self.sex = sex
		self.age = age
	def feed(self):
		return print(self.name.title() + " is grabbing something to eat!")
	def sleep(self):
		return print(self.name.title() + " is getting ready to take a nap.")

class Dog(Pet):
	def __init__(self):
		Pet.__init___(self) #inheritance line
		self.favorite_food = favorite_food


#create a Timer class
class Timer:
	def __init__(self,hours = 0, minutes = 0, seconds = 0):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds



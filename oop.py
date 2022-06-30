class Fish:
	def __init__(self,name):
		self.name = name
		self.canswim = True
		self.isscalar = True
class Trout(Fish):
	def __init__(self,name):
		super().__init__(name)
		self.type_ = type_
		self.pref_watertemp = 65
	def greeting(self):
		print("Howdy! I'm a trout! I'm the best kind of fish in the world!")



class ExampleClass:
	somelist = [1,2,3,4,5,6]
	def __init__(self,name):
		import random as r
		self.name = name
		try:
			assert type(self.name) == str
		except AssertionError as ae:
			print("Your name must be a string!")
		self.number = r.choice(ExampleClass.somelist)

# instance = ExampleClass("Will")
# print(instance.number)

import sys
print(sys.os)
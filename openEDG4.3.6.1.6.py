# class FishError(Exception):
# 	def __init__(self,fish,message):
# 		super().__init__(message)
# 		self.fish = fish

class FishError(Exception):
	pass

#import random module
import random

#create fish weighing funtcion
def fishweigh(fish):
	randomweight = random.randint(7,10)
	if randomweight > 6:
		raise FishError("this fish is too heavy!")
	else:
		return print(randomweight)

#now test the function
try:
	fishweigh("Trout")
except FishError as fe:
	print(fe)

class Restaurant(object):
	
	""" My representation of a restaurant.""" 
	def __init__(self, restaurant_name, cuisine_type,flavors):
		"""Initialize name and cuisine type attributes."""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0 
		self.flavors = flavors
	
	def describe_restaurant(self):
		print(self.restaurant_name + " serves " + self.cuisine_type + ". " + self.restaurant_name + " has served " + str(self.number_served) + " people.")
	
	def open_restaurant(self):
		print(self.restaurant_name + " is now open!")
	def add_number_served(self, number):
		self.number_served += number


class IceCreamStand(Restaurant):

	def __init__(self,restaurant_name,cuisine_type,flavors):
		super(IceCreamStand,self).__init__(restaurant_name,cuisine_type,flavors)
		
	
	def display_flavors(self):
		for i in self.flavors:
			print(self.restaurant_name + " serves " + i + ' icecream.')

dairy_queen = IceCreamStand("Dairy Queen", "icecream", ["Chocolate", "Vanilla", "Strawberry"])
dairy_queen.number_served = 80
dairy_queen.add_number_served(40)
dairy_queen.display_flavors()
dairy_queen.describe_restaurant()
import sys
print(sys.version)





















class Restaurant(object):
	def __init__(self,restaurant_name,cuisine_type,number_served):
		self.restaurant_type = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = number_served
	def restaurant_describe(self):
		print(self.restaurant_name.title() + " serves " + self.cuisine_type + ". It has served " + self.number_served + " people!")
	def number_served_update(self, update_num):
		self.number_served += update_num
class IceCreamStand(Restaurant):
	def __init__(self,restaurant_name,cuisine_type,number_served):
		super(IceCreamStand,self).__init__(restaurant_name,cuisine_type,number_served)
		self.flavor = ["Chocolate","Vanilla"]
	def flavor_print(self):
		for i in self.flavor:
			print(self.restaurant_name + " serves " + i + " icecream.")
dairy_queen = IceCreamStand("Dairy Queen","icecream",250)
dairy_queen.flavor_print()



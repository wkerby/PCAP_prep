class Car(object):
	def __init__(self, make, model, year):
		#initialize attributes to describe a car
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		#return a neatly formatted descriptive name
		print(str(self.year) + " " + self.make + " " + self.model)

	def update_odometer_reading(self,mileage):
		self.odometer_reading = mileage
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")
	def read_odometer(self):
		print("Your car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car("Toyota", "4Runner", 2017)

my_new_car.get_descriptive_name()
my_new_car.update_odometer_reading(17000)
my_new_car.read_odometer()

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super(ElectricCar,self).__init__(make, model, year)
		self.battery_size = 70
	def change_battery_size(self,battery_size):
		self.battery = battery_size
my_brand_new_car = ElectricCar("Tesla", "Model S", 2019)
my_brand_new_car.get_descriptive_name()
my_brand_new_car.update_odometer_reading(40)
my_brand_new_car.read_odometer()


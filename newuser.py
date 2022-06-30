class User():
	def __init__(self,first_name,last_name,age,fav_color):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.fav_color = fav_color
	def describe_user(self):
		print("First name: " + self.first_name.title() + "\n" + "Last name: " + self.last_name.title() + "\n" + "Age: " + str(self.age) + "\n" + "Favorite color: " + self.fav_color.title())
	def greet_user(self):
		print("Hello, " + self.first_name.title() + "! Welcome to the world of Python.")

Me = User("will","kerby", 24, "green")

Me.describe_user()

You = User("clay","kerby", 24, "blue")

You.describe_user()


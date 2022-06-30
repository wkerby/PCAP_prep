#test inheritance for a subclass
class Cat:
	def __init__(self, name, age, sex):
		self.name = name
		self.age = age
		self.sex = sex
		if sex not in ["male","female","male".title(),"female".title(),"m","f"]:
			print("The cat must be male or female")
		else:
			self.sex = sex
		if sex in ["male","male".title(),"m"]:
			self.pronoun = "he"
		else:
			self.pronoun = "she"
		

	def meow(self):
		try:
			print(self.name.title() +  " is hungry!" + self.pronoun + " needs more food.")
		except AttributeError:
			print("Your cat is neither male nor female. Sorry!")

class Tabby(Cat):
	def __init__(self,name,age,sex):
		super().__init__(name,age,sex)
i = 1
for z in list(range(2500)):
	i+=7
print(i)
#create a week class according to directions in Open EDG 3.4.1.13
class Weeker():
	__weekdays = {"Mon":[1,list(range(1,17502,7))], "Tue":[2,list(range(2,17503,7))], "Wed":[3,list(range(3,17504,7))], 
	"Thu":[4,list(range(4,17505,7))], "Fri":[5,list(range(5,17506,7))], "Sat":[6,list(range(6,17507,7))], "Sun":[7,list(range(7,17508,7))]}
	def __init__(self, __weekday):
		self.__weekday = __weekday
		try:
			assert self.__weekday in list(Weeker.__weekdays.keys())
		except AssertionError:
			print("Sorry, I can't serve your request.")
		self.__weekdaynum = Weeker.__weekdays[self.__weekday][0]
	def add_(self,n=1):
		if type(n) != int:
			print("This is not an acceptable value. Please enter an integer.")
		else:
			self.__weekdaynum += n
			for day in list(Weeker.__weekdays.keys()):
				if self.__weekdaynum in Weeker.__weekdays[day][1]:
					self.__weekday = day
	def sub_(self, n=1):
		if type(n) != int:
			print('This is not an acceptable value. Please enter an integer.')
		elif self.__weekdaynum == 1:
			print("You can't go back in time!")
		else:
			self.__weekdaynum -= 1
			for day in list(Weeker.__weekdays.keys()):
				if self.__weekdaynum in Weeker.__weekdays[day][1]:
					self.__weekday = day
	def disp(self):
		print(self.__weekday)

#verify that the methods work as intended
exampleobject = Weeker("Thu")
exampleobject.disp()
print("Now begin test:")
for i in list(range(50)):
	exampleobject.sub_()
	exampleobject.disp()


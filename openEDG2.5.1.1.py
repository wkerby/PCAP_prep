# #question 14
# class Calculate:
# 	var1 = 20
# 	def __init__(self,var1):
# 		self.var1 = var1
# 		self.var1 += 7
# 		Calculate.var1 += 7
# 	def printer(self):
# 		print(Calculate.var1)
# 		print(self.var1)

# instance1 = Calculate(19)
# instance1.printer()
# instance2 = Calculate(1)
# instance2.printer()

# #question 15
# try:
# 	tuple = [1,2,3,4]
# 	print(tuple[3])
# except TypeError as te:
# 	print("This is a type error")

# #question 16
# x = 45
# y = 25

# def Sum(x):
# 	global x #this line will raise a SyntaxError
# 	print("Sum inside of Sum() :", x+y)
# Sum(25)
# print("Sum outside of Sum() :", x+y)

import random
x = random.randint(1,6)
match x:
	case 1:
		print("%s answer is 1" % "The")
	case 2: 
		print("%s answer is 2" % "The")
	case _:
		print("%s answer is neither 1 nor 2" % "The")

import platform
print(platform.machine())
print(platform.node())
print(platform.platform())
print(platform.version())
print(platform.system())
print(platform.python_version_tuple())
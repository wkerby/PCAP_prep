#create a customized error from the ZeroDivisionError class that prohibits division by any number from 1 to 100
class NumberDivisionError(ZeroDivisionError):
	def __init__(self,number,message):
		super().__init__(self,message)
		self.number = number

#create a customized error from the ZeroDivisionError class that prohibits division by 1
class OneDivisionError(ZeroDivisionError):
	pass

def divider(num, denom):
	if denom in range(2,101):
		raise NumberDivisionError(denom, "you cannot divide by this number")
	elif denom == 1:
		raise OneDivisionError("division by one")
	else:
		return num/denom

#test the created NumberDivisionError
for i in range(88,102):
	try:
		divider(100,i)
	except NumberDivisionError as nde:
		print(nde, ":", nde.number)

#test the created OneDivisionError
for i in range(2):
	try:
		divider(3,i)
	except ZeroDivisionError as zde:
		print(zde)
	except OneDivisionError as ode:
		print(ode)









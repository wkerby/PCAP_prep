#test the global keyword
def somefunction(par):
	loc = par
	def inner():
		return loc
	return inner
var = 1
newvar = somefunction(var)
print(newvar())

#create a function creator for adding a specified constant to a specified value making use of a closure
def add_create(addvalue):
	add = addvalue
	def closure(somevalue):
		return somevalue + add
	return closure
addone = add_create(1)
print(addone(3))

#create a function creator for multiplying a number by a specified constant making use of a closure
def multiply_create(multvalue):
	mult = multvalue
	def multiply(somevalue):
		return somevalue * mult
	return multiply

multiply_three = multiply_create(3)
print(multiply_three(8))

#create a function creator for subtracting a specified constant to a specified value making use of a closure
def subtract_function(subtractvalue):
	subtract = subtractvalue
	def closure(somevalue):
		return somevalue - subtract
	return closure

#create a function creator that squares a value by a constant making use of a closure
def powercreator(expvalue):
	exp = expvalue
	def raiseto(someconstant):
		return someconstant**exp
	return raiseto

#validate that the creator function works as intended
square = powercreator(2)
cube = powercreator(3)

for i in range(5):
	print(square(i), cube(i))

#open a file strictly for creation
try:
	with open(r"Z:\\Users\\WKerby\\My Computer\\Documents\\testfile.txt",'w') as teststream:
		teststream.write("with open(filename, 'wt') as fileobject:\n\tfileobject.write(\"something stupid\")")

except Exception as exc:
	print("Unable to function:",exc)

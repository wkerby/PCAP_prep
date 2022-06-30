def slopefinder(point1,point2):
	for tup in [point1,point2]:
		try:
			assert len(tup) == 2
			assert type(tup) == tuple
		except AssertionError:
			return print("You must enter two tuples representing two (X,Y) cartesian points.")
	slope = (point2[1]-point[1])/(point2[0]-point1[0])
	return slope

def add(a,b,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0,m=0,n=0,p=0,q=0):
	sum_ = 0
	for num in [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q]:
		try:
			assert type(num) == float or type(num) == int
		except AssertionError:
			return print("You must enter integer or float values into the function.")
		sum_+= num
	return sum_

def divide(a,b):
	for num in [a,b]:
		try:
			assert type(num) == float or type(num) == int
		except AssertionError:
			return print("You must enter integer or float values into the function.")
	return a/b


class ExampleClass:
    varia = 1
    def __init__(self, val):
        varia = val

example_object = ExampleClass(2)
print(example_object.varia)
print(ExampleClass.__dict__)
print(example_object.__dict__)

#create a closure for adding a number to a value
def addby(num):
	par = num
	def addnum(somenum):
		return somenum + par
	return addnum

addby3 = addby(3)
print(addby3(8))
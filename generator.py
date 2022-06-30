#create a manual generator that resembles the range() generator
class TestRange:
	def __init__(self,n):
		self.n = n
		self.i = 0
	def __iter__(self):
		return self
	def __next__(self):
		self.i += 1
		if self.i > self.n:
			raise StopIteration
		else:
			return self.i - 1 

#verify the generator works as intended
print(list(TestRange(9)))

#now create a generator for the fibonacci sequence, making use of the yield keyword
def fibonacci(n):
	try:
		assert n > 0
	except AssertionError:
		print("You must provide non-negative integer greater than 0.")
	else:
		p1 = 1
		p2 = 1
		for i in range(1,n+1):
			if i == 1:
				yield p1
			elif i == 2:
				yield p2
			else:
				yield p1 + p2
				p1,p2 = p2,p1+p2

#verify that the generator works as intended
print([i for i in fibonacci(9)])

#test the map function
print(list(map(lambda x: x*2, [i for i in range(9)])))

#count the number of characters in a text file using python
filename = r'Z:\\Shared\\Users\\WKerby\\My Computer\\Documents\\Python\\testfile.txt'
with open(filename, 'r') as fileobject:
	readlist = list(fileobject.read())

#create a block of code that writes 10 lines into a new .txt file
filename_ = r"Z:\\Shared\\Users\\WKerby\\My Computer\\Documents\\Python\\writefile.txt"
with open(filename_, "w") as fileobject:
	numlines = 0
	for i in range(1,11):
		someline = "Line #" + str(i) + "\n"
		numlines += 1
		for char in someline:
			fileobject.write(char)
	fileobject.write("Number of lines: " + str(numlines))

data = bytearray(10)
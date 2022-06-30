#create a function that reads a file of student points and returns the total number of points per student
#create custom errors
#file's non-existence
class NoFileError(Exception):
	def __init__(self):
		super().__init()
		self.printedmessage = "This is a custom error message. No such file exists!"
#file's emptiness
class EmptyFileError(NoFileError):
	def __init__(self,printedmessage):
		super().__init()
		self.printedmessage = "This is another custom error message. The file you are referencing is empty!"

#read lines in the text file
filename = r"Z:\\Users\\WKerby\\My Computer\\Documents\\Python\\empty.txt"
with open(filename, 'r') as fileobject:
	line_modify = []
	lines = fileobject.readlines()
	for line in lines:
		if line == "\n":
			pass
		else:
			line = line.split('\t')














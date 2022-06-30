#create a script that takes a .txt file name as input and returns a histogram of the count of each letter that appears in file
import pygal as pyg
import os

#read the txt file and store counts in a dictionary
try:
	filename = input("Please provide a file path:")
	alphas = 'abcdefghijklmnopqrstuvwxyz'
	lettercount = {}
	for letter in alphas:
		lettercount[letter] = 0
	with open(filename, 'r') as fileobject:
		lines = fileobject.readlines()
		for line in lines:
			for char in line:
				if char.lower() in list(lettercount.keys()):
					lettercount[char.lower()] += 1

	#sort the dictionary highest frequency letter --> lowest frequency letter
	sortlist = sorted(list(lettercount.items()),key = lambda x:x[1],reverse = True)
	letters = []
	counts = []
	for letter,count in sortlist:
		letters.append(letter)
		counts.append(count) 
                
	#now create histogram of the results
	txthist = pyg.Bar()
	txthist.title = "Letter Frequency Histogram"
	txthist.x_labels = letters
	txthist.x_title = "Letter"
	txthist.y_title = "Frequency"
	txthist.add(None, counts)
	txthist.render_to_file(r'Z:\\Shared\\Users\\WKerby\\My Computer\\Documents\\Python\\lettercountvis.svg')
except Exception as e:
	print("Shit hit the fan: ", os.strerror(e.errno))

#create a function that lets user know whether the word provided in first argument is
#hidden within the combination of characters given in the second argument
def findaword(string1,string2):
	string1 = string1.lower()
	string2 = string2.lower()
	find_indices = []
	for char in string1:
		if char == string1[0]:
			if char in string2:
				start = string2.find(char)
				find_indices.append(string2.find(char))
			else:
				return print("No")
				break
		else:
			if string2.find(char,start) not in find_indices:
				find_indices.append(string2.find(char, start))
			else:
				find_indices.append(string2.find(char, find_indices[-1]))
	if -1 in find_indices:
		return print("No")
	else:
		for i in list(range(len(find_indices)-1,0,-1)):
			if find_indices[i] - find_indices[i-1] < 0:
				return print("No")
				break
		return print("Yes")

findaword("donut","Nabucodonosor")



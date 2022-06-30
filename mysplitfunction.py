def mysplit(some_string):
	string_dict = {}
	for i in list(range(len(some_string))):
		string_dict[i] = some_string[i]
	spaces = [i for i,x in list(string_dict.items()) if x.isspace() == True]
	split_list = []
	if len(spaces) == 0:
		split_list.append(some_string)
	else:
		for i in spaces:
			if len(spaces) == 1:
				split_list.append(some_string[:i])
				split_list.append(some_string[i+1:])
				break
			else:
				if i == spaces[0]:
					split_list.append(some_string[:i])
					z = 0
				elif i in spaces[1:len(spaces)]:
					beg_index = spaces[z] + 1
					# beg_index = spaces[spaces.index(i-1)]
					end_index = spaces[z+1]
					# end_index = spaces[spaces.index(i-1)+1]
					split_list.append(some_string[beg_index:end_index])
					z += 1
					if z == len(spaces) - 1:
						split_list.append(some_string[i+1:len(some_string)])

	#remove any fragments that represent blank space
	for i in list(range(len(split_list))):
		for frag in split_list:
			if bool(frag) == False:
				split_list.remove(frag)

	return split_list

print(mysplit('    '))
print(mysplit("Score a goal for Swansea."))
print(mysplit("Swansea"))
print(mysplit("a goal."))
print(mysplit(' abc '))
print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))




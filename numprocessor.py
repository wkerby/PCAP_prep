#create a number processor function
active = True
quitlist = ["q", "Q", "quit", "quit".upper(), "quit".title()]
while active == True:
	line = input("Enter a line of numbers - separate them with spaces: ")
	if line in quitlist:
		active = False
		break
	strlist = line.split()
	sum_ = 0
	try:
		for strnum in strlist:
			sum_ += int(strnum)
	except:
		print("Thats not a valid set of numbers!")
	else:
		if len(strlist) == 1:
			print("Make sure to separate your numbers with spaces should you want to sum more than one number.")
		print(sum_) 

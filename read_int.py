#define a function that raises an error when integer enter is either a) not an integer or b) not in the domain specified in 
#the function
check = "test string"
def read_int(prompt, min_, max_):
	global check
	check = input(prompt)
	int_ = int(check) #ValueError could be raised here
	if int_ not in list(range(min_,max_+1)):
		return print('Value not within the range of ',str(min_),"and",str(max_)+"!")
	else:
		return print("The number is: " + str(int_) + "!")

active = True
while active == True:
	try:
		read_int("Enter a number between -2 and 100:",-2,100)
	except:
		if check in ["q","Q","quit","Quit","QUIT"]:
			print("Thanks for testing!")
			active = False
		else:
			print("Please enter an integer value.")

			




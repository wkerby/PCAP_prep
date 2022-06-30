#create a function that detects palindromes
def palindrome(string):
	string = string.replace(' ','').lower()
	check_pal = ""
	for char in string:
		if char == "\n":
			return print("String must be one line long.")
			break
	for i in list(range((len(string)-1),-1,-1)):
		check_pal += (string[i])
	if check_pal == string:
		return print("The string is a palindrome.")
	else:
		return print("The string is not a palindrome.")

palindrome("Racecar")



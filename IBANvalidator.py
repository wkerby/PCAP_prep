#create an IBAN vaildator function
def IBANvalid(IBAN):
	IBAN = IBAN.replace(' ', '')
	for char in IBAN:
		if not char.isalnum():
			return print("Your IBAN contains invalid characters.")
	IBAN = (IBAN[4:] + IBAN[:4]).upper()
	if len(IBAN) < 15 or len(IBAN) > 31:
		return print("The IBAN you entered contains an invalid number of characters.")
	else:
		sumiban = 0
		for char in IBAN:
			if char.isdigit():
				sumiban += int(char)
			else:
				sumiban += (10 + (ord(char)-ord("A")))
		if sumiban % 97 == 1:
			return print("The IBAN you entered is valid.")
		else:
			return print("The IBAN you entered is invalid.")
IBANvalid("LU 28 001 9400644750000")


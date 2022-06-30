#test the continue and the pass function
#using the pass keyword
for i in range(1,6):
	if i == 1:
		pass
	print(i, end = "-")
#using the continue keyword
for i in range(1,6):
	if i == 1:
		continue
	print(i, end = "-")
#using the break keyword
for i in range(1,6):
	if i == 1:
		break
	print(i, end = "-")
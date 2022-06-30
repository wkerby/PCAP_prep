#import the random module
import random

#create a function that takes a 9x9 matrix of numbers (a nine-line string)
#and checks for sudoku validity
def sudoku(string):
	lines = 1
	for i in string:
		if i == "\n":
			lines += 1
	if lines != 9:
		return print("You must enter a 9x9 matrix of numbers.")
	else:
		valid = [1,2,3,4,5,6,7,8,9]
		string = string.replace("\t","").replace(' ', '')
		string = string.split("\n")
		matrix = []
		for str_ in string:
			strlist = []
			for s in str_:
				strlist.append(int(s))
			matrix.append(strlist)
		print("validate rows")
		#validate across rows (left-to-right)
		for row in matrix:
			check_list = []
			for num in row:
				check_list.append(int(num))
			check_list.sort()
			if check_list == valid:
				continue
			else:
				return print("No")
		print("validate columns")
		#validate across columns (up-and-down)
		column = 0
		while column <= 8:
			check_list = []
			for row in list(range(len(matrix))):
				check_list.append(int(matrix[row][column]))
			check_list.sort()
			if check_list == valid:
				column += 1
				continue
			else:
				return print("No")
		#validate by each 3x3 submatrix
		print("validate submatrices")
		row_columns = {}
		index_choices = [(0,1,2),(3,4,5),(6,7,8)]
		for i in list(range(1,(len(index_choices)**2)+1)):
			row_columns[i] = []
		while [] in list(row_columns.values()):
			row_column = []
			for i in list(range(2)):
				row_column.append(random.choice(index_choices))
			if row_column not in list(row_columns.values()):
				row_columns[[key for key,value in list(row_columns.items()) if value == []][0]] = row_column
		for i in list(row_columns.keys()):
			submatrix = []
			rows = row_columns[i][0]
			columns = row_columns[i][1]
			for row in rows:
				for column in columns:
					submatrix.append(matrix[row][column])
			submatrix.sort()
			if submatrix == valid:
				continue
			else:
				return print("No")
	return print("Yes")

sudoku("""123456789
	      123456789
	      123456789
	      123456789
	      123456789
	      123456789
	      123456789
	      123456789
	      123456789""")


sudoku("""295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672""")

sudoku("""195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671""")

		


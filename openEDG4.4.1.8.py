#test methods in the os module
import os

#create a functiont that searches for a specified directory within a specified file path
def findfolder(dir_,path):
	startpath = path
	try:
		os.chdir(startpath)
		dir_contents  = os.listdir(startpath)
		if dir_ in dir_contents:
			return print("The", dir_, "folder is in the following path:", path)
		else:
			for content in dir_contents:
				extension_search = content.split(".")
				if len(extension_search) == 1:
					path = startpath + "\\" + extension_search[0]
					findfolder(dir_,path)
				else:
					pass
	except OSError:
		pass

findfolder("Modules",r"Z:\\Users")

# print(os.listdir(r"Z:\\Users\\WKerby\\My Computer\\Documents\\Python"))
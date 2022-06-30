import os
os.chdir(r"C:\\Users\\wkerb\\AppData\\Roaming\\Sublime Text\\Packages")
# os.mkdir("CMD")

# filename = r"C:\\Users\\wkerb\\AppData\\Roaming\\Sublime Text\\Packages\\CMD\\cmd.py"
# with open(filename, "x") as file_object:
# 	pass

filename = r"C:\\Users\\wkerb\\AppData\\Roaming\\Sublime Text\\Packages\\CMD\\Context.sublime-menu"
with open(filename, "x") as file_object:
	pass

with open(filename, "w") as file_object:
	file_object.write('{ "command": "cmd" }')



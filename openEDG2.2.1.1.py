#example of when to use the escape \
mystring = 'I\'m a cowboy. On a steel horse I ride.'
print(mystring)

#the two strings have equal output
myotherstring = "All hail the\nwhite rectangle!"
myotherotherstring = '''All hail the 
white triangle!'''

#practice using the .join() string method
examplestring = "****".join(['foo', 'fighters']) #the one argument passed is a list containing the substrings that will be joined
print(examplestring)

#another example
rhcp = "".join(list("red hot chili peppers"))
print(rhcp)
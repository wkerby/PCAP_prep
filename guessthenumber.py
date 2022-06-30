from random import *

loopval = 0
x = str(int(uniform(1,4)))

while loopval == 0:

    value1 = input("Guess any number between 1 and 4:")

    if value1 == x:
        print("You guessed correctly!")
        loopval = 1
        
    else:
        loopval = 0
        print("Wrong guess! Try again.")
        



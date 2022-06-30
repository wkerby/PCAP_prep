value1 = input("Player 1 enter your player type: ")
value2 = input("Player 2 enter your player type: ")
x = []

if value1 == "Rock" and value2 == "Paper":
    x = 2

elif value1 == "Paper" and value2 == "Paper":
    x = 3

elif value1 == "Scissors" and value2 == "Paper":
    x = 1

elif value1 == "Rock" and value2 == "Scissors":
    x = 1
elif value1 == "Paper" and value2 == "Scissors":
    x = 2
elif value1 == "Scissors" and value2 == "Scissors":
    x = 3
elif value1 == "Rock" and value2 == "Rock":
    x = 3
elif value1 == "Paper" and value2 =="Rock":
    x = 1
elif value1 == "Scissors" and value2 == "Rock":
    x = 2

if x == 1:
    print("Player 1 is the winner!")
if x == 2:
    print("Player 2 is the winner!")
if x == 3:
    print("We have a tie!")
    




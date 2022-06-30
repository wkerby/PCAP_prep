from random import *
class Die():
    def __init__(self, num_sides = 6):
        self.num_sides = num_sides
    def dice_roll(self):
        return randint(1,self.num_sides)

die = Die()
roll_list = [die.dice_roll() for i in list(range(0,1000))]
#print(roll_list)

def num_count(mylist,number):
    count = 0
    for i in mylist:
        if i == number:
            count += 1
        else:
            continue
    return count

die1 = Die()
die2 = Die(10)

different_roll_list = [die1.dice_roll() + die2.dice_roll() for i in list(range(0,50000))]
different_count_list = []
for i in list(range(2,17)):
    different_count_list.append(num_count(different_roll_list,i))


import pygal
histogram = pygal.Bar()
histogram.title = "Results of D6 + D10 die role"
histogram.x_lables = ["2","3", "4", "5","6","7","8","9","10","11","12","13","14","15","16"]
histogram.x_title = "Result"
histogram.y_title = "Result frequency"
histogram.add("D6 + D10", different_count_list)
histogram.render_to_file("different_die_visual.svg")

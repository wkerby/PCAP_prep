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

count_list = []
for i in list(range(1,7)):
    count_list.append(num_count(roll_list, i))
#print(count_list)

    
import pygal
histogram = pygal.Bar()
histogram.title = "Results of D6 die role"
histogram.x_labels = ["1","2", "3", "4","5","6"]
histogram.x_title = "Result"
histogram.y_title = "Result frequency"
histogram.add("D6", count_list)
histogram.render_to_file('die_visual.svg')






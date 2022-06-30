import matplotlib.pyplot as plt
#plotting a simple line graph
#xvalues = [1,2,3,4,5]
#yvalues = [1,4,9,16,25]
#plt.plot(xvalues, yvalues,linewidth = 5)
#set chart title and label axes
#plt.title("Square Numbers",fontsize = 22)
#plt.xlabel("Value", fontsize = 12)
#plt.ylabel("Square of Value", fontsize = 12)
#set size of tick labels
#plt.tick_params(axis = 'both', labelsize = 12)
#display the graph
#lt.show()

#plot cube numbers
#x_values = list(range(1,6))
#y_values = [x**3 for x in x_values]
#plt.scatter(x_values, y_values, s = 40)
#plt.show()

#x2_values = list(range(1,1001))
#y2_values = [x2**3 for x2 in x2_values]
#plt.scatter(x2_values,y2_values)
#plt.show()

#from random import choice
#class RandomWalk():
	#def __init__(self,num_points = 5000):
		#self.num_points = num_points
	#all walks start at (0,0)
		#self.x_values = [0]
		#self.y_values = [0]

	#def fill_walk(self):
		#while len(self.x_values) < self.num_points:
			#x_direction = choice([-1,1])
			#x_distance = choice([0,1,2,3,4])
			#x_step = x_direction*x_distance
			#y_direction = choice([-1,1])
			#y_distance = choice([0,1,2,3,4])
			#y_step = y_direction*y_distance
			#next_step_x = self.x_values[-1] + x_step
			#next_step_y = self.y_values[-1] + y_step
			#self.x_values.append(next_step_x)
			#self.y_values.append(next_step_y)


#my_random_walk = RandomWalk(500)
#my_random_walk.fill_walk()
#print(my_random_walk.x_values)
#print(my_random_walk.y_values)


#exercise 15.3 - Molecular Motion
#plt.plot(my_random_walk.x_values,my_random_walk.y_values,linewidth = 2)
#plt.show()



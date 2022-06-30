#create a class that displays time in HH:MM:SS format and increments time by +- 1 second
class Timer:
	def __init__(self, hour = 0, minute = 0, second = 0):
		self.hour = hour
		self.minute = minute
		self.second = second
		try: 
			assert self.hour in list(range(24))
		except AssertionError:
			print("This is not a feasible time.")
		try:
			assert self.minute in list(range(60))
		except AssertionError:
			print("This is not a feasible time.")
		try: 
			assert self.second in list(range(60))
		except AssertionError:
			print("This is not a feasible time.")
	def reset(self):
		self.hour = 0
		self.minute = 0
		self.second = 0
	def next_second(self):
		self.second += 1
		if self.second == 60:
			self.second = 0
			self.minute += 1
		if self.minute == 60:
			self.minute = 0
			self.hour += 1 
		if self.hour == 24:
			self.reset()
	def prev_second(self):
		self.second -= 1
		if self.second < 0:
			self.second = 59
			self.minute -= 1
		if self.minute < 0:
			self.minute = 59
			self.hour -= 1
		if self.hour == -1:
			self.hour = 23
	def printable(self):
		if len(str(self.hour)) == 2 and len(str(self.minute)) == 2 and len(str(self.second)) == 2:
			print(str(self.hour) + ":" + str(self.minute) + ":" + str(self.second))
		elif len(str(self.hour)) == 2 and len(str(self.minute)) == 2 and len(str(self.second)) == 1:
			print(str(self.hour) + ":" + str(self.minute) + ":0" + str(self.second))
		elif len(str(self.hour)) == 2 and len(str(self.minute)) == 1 and len(str(self.second)) == 1:
			print(str(self.hour) + ":0" + str(self.minute) + ":0" + str(self.second))
		elif len(str(self.hour)) == 1 and len(str(self.minute)) == 1 and len(str(self.second)) == 1:
			print("0" + str(self.hour) + ":0" + str(self.minute) + ":0" + str(self.second))
		elif len(str(self.hour)) == 1 and len(str(self.minute)) == 1 and len(str(self.second)) == 2:
			print("0" + str(self.hour) + ":0" + str(self.minute) + ":" + str(self.second))
		elif len(str(self.hour)) == 1 and len(str(self.minute)) == 2 and len(str(self.second)) == 1:
			print("0" + str(self.hour) + ":" + str(self.minute) + ":0" + str(self.second))
		elif len(str(self.hour)) == 2 and len(str(self.minute)) == 1 and len(str(self.second)) == 2:
			print(str(self.hour) + ":0" + str(self.minute) + ":" + str(self.second))
		else:
			print("0" + str(self.hour) + ":" + str(self.minute) + ":" + str(self.second))

#verify that the next_second() and prev_second() methods work
timeriter = 24*60*60 + 1
nextimer = Timer()
nextimer.printable()
print("Begin test:")
time_list = list(range(timeriter))
for i in time_list:
	nextimer.prev_second()
	nextimer.printable()





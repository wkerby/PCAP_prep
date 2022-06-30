#create the MyCalendar subclass of the Calendar class that counts the number of total days of a certain weekday (e.g. Wednesday) in a year
import calendar
class MyCalendar(calendar.Calendar):
	# def __init__(self,firstweekday):
	# 	super().__init__(firstweekday)
	def count_weekdays_in_year(self,year,weekday):
		daycount = 0
		for month in range(1,13):
			for week in self.monthdays2calendar(year,month):
				for tup in week:
					if tup[0] == 0:
						pass
					else:
						if tup[1] == weekday:
							daycount += 1
		return daycount

myobj = MyCalendar(calendar.SUNDAY)
print(myobj.count_weekdays_in_year(2021,4))

	

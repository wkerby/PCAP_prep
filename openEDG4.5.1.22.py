#import the datetime class from the datetime module
from datetime import datetime as dt
datetime_obj = dt(2020, 11, 4, 14, 53)

#use different directives to display this datetime obect in different formats
print(datetime_obj.strftime("%Y/%m/%d %H:%M:%S")) #format 1
print(datetime_obj.strftime('%y/%B/%d %H:%M:%S %p')) #format 2
print(datetime_obj.strftime('%a, %Y %b %d')) #format 3
print(datetime_obj.strftime('%A, %Y %B %d')) #format 4
print(datetime_obj.strftime('Weekday: %w')) #format 5 
print(datetime_obj.strftime('Day of the year: %j')) #format 6
print(datetime_obj.strftime('Week number of the year: %U')) #format 7


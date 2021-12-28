#Method 2
from datetime import date
from datetime import datetime
#Show current time
today=date.today()
time=datetime.now()
print("today's date is ",today)
print('Time is ',time)
print("2018-06-29 08:15:27")
entertime= input("Enter the time of the day (yyyy-mm-dd hh:mm:ss)")
timetaken=datetime.strptime(entertime, '%Y-%m-%d %H:%M:%S')
print("Date: ", timetaken.date())
print("Time: ", timetaken.time())
#


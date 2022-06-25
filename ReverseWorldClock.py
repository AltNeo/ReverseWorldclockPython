#Method 2
import json
import re
from datetime import date, datetime, timezone
import pytz
import timezonefinder
tzf=timezonefinder.TimezoneFinder()

from urllib.request import urlopen

#Show current time
today=date.today()
timethen=datetime.now().replace(microsecond= 0)
print("today's date is ",today)
print('Time is ',timethen)
print("A sample date to input")
print("2021-12-29 11:28:00")
entertime= input("Enter the time of the day (yyyy-mm-dd hh:mm:ss)")
timetaken=datetime.strptime(entertime, '%Y-%m-%d %H:%M:%S')
print("Date: ", timetaken.date())
print("Time: ", timetaken.time())
if str(timetaken) > str(timethen):
    timediff=str(timetaken -timethen)
    ahead=1
    print('Time Difference=', str(timetaken -timethen))
    print("We know the region is in west")
else:
    timediff=str(timethen-timetaken)
    ahead=0
    print('Time Difference=', str(timethen-timetaken))
    print("So we know that the region is in east")
print('Total difference in minutes: ', timediff)
timedifflist=timediff.split(":")
#print(timedifflist)
totalmins=(int(timedifflist[0])*60)+int(timedifflist[1])
#print(totalmins)


## Now for the Part 2 of the project.
## Part 2 a)
## Getting Ip of the user.
url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

IP=data['ip']
org=data['org']
city = data['city']
country=data['country']
region=data['region']

#print(IP)


#getting co-ordinates from ip
tzlist=[]
url= 'http://ip-api.com/json/'+IP
response= urlopen(url)
data= json.load(response)
longitude=int(data.get('lon'))
#print(longitude)
if ahead ==1:
    longitude=longitude+(totalmins/4)
    for latitude in range (1,91,10):
        timezone=tzf.certain_timezone_at(lat=latitude,lng=longitude)
        tzlist.append(timezone)
    tzlist=list(dict.fromkeys(tzlist))        
    print(tzlist)
else :
    longitude=longitude-(totalmins/4)
    for latitude in range (1,91,5): 
        timezone=tzf.certain_timezone_at(lat=latitude,lng=longitude)
        tzlist.append(timezone)
    tzlist=list(dict.fromkeys(tzlist))        
    print(tzlist)
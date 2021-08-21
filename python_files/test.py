from datetime import date,datetime
import time

print(str(datetime.now().date()))

print(int(time.mktime(datetime.strptime("2021-08-13", "%Y-%m-%d").timetuple())))

print(time.mktime(datetime.strptime(str(date.today()), "%Y-%m-%d").timetuple())+86400)
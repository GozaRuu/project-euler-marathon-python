#!/usr/bin/env python

import datetime

#simple solution to this otherwis tedious problem using python datetime library,
#just add 1 day between 2 datetime objects and count results

time_delta, res = datetime.timedelta(days=1), 0
y1, m1, d1 = 1901,1,1
y2, m2, d2 = 2000,12,31
a = datetime.datetime(y1, m1, d1)
b = datetime.datetime(y2, m2, d2)

# the datetime library have constraints for the size of the input you can put. so,
# we use this trick to solve the HackerRank constraint which years can be around
#10**17, the calender laps every 400 years so we can just start from 400 + y1%400
#to 400 + y1%400 + y2-y1 (starting from year 0 might be risky) :

# dY = y2-y1 #num of years
# y1 = (y1%400) + 400 #normalized and non-zero
# a = datetime.datetime(y1, m1, d1)
# b = datetime.datetime(y1+dY, m2, d2)

while a <= b:
	if a.day == 1 and a.weekday() == 6: res += 1; time_delta = datetime.timedelta(days=7)
	a += time_delta

print res

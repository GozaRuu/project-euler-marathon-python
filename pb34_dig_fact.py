#!/usr/bin/env python
from math import factorial
factorials = [ factorial(i) for i in xrange(10)]
#ez

# n = int(raw_input().strip())
n = 10**5+1
res = 0
# for i in xrange(10, n): #hackerRank
for i in xrange(3, n):
    # if sum(map(lambda x:factorials[x], map(lambda x:int(x), str(i)))) % i == 0: res += i #hackerRank
    if sum(map(lambda x:factorials[x], map(lambda x:int(x), str(i)))) == i: res += i
print res

#!/usr/bin/env python
from bisect import bisect_left

#using binary search to solve this problem especially the HackerRank version which has huge limits for a simple bruteforce search

d = [0] * 28124
for i in xrange(1, 28124):
    for j in xrange(2*i,28124,i):
        d[j] += i

abund = []
for i in xrange(1,28124):
        if d[i]>i: abund.append(i) #we know for sure abund will be sorted for us from the way we construct it



# t  = int(raw_input().strip())
# for _ in xrange(t):
#     n = int(raw_input().strip())
#     done = False
#     i = 0
#     while not done and i < min(n,len(abund)):
#         if n - abund[i] > 28123  or abund[bisect_left(abund, n - abund[i])] == n - abund[i]: print "YES" ; done = True
#         i += 1
#     if not done: print "NO"


res = 0
for n in xrange(1,28124):
    i = 0
    done = False
    while not done and i < min(n, len(abund)):
        if abund[bisect_left(abund, n - abund[i])] == n - abund[i]: done = True
        i += 1
    if not done: res += n

print res

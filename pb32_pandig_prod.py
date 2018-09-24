#!/usr/bin/env python
from itertools import permutations
#just a bruteforce solution in order O(100*9!) it works even for HackerRank only timesout in the last case
#the HackerRank variation of the problem is not that much different it just varies n from 4 to 9

res = set()
n = 9
#for HackerRank just do:   if n == 9: print 45228
for p in permutations(range(1,n+1)):
    p = ''.join(map(lambda x:str(x), p))
    for i in xrange(1,n-1):
        for j in xrange(i+1,n):
            if int(p[:i]) * int(p[i:j]) == int(p[j:]):
                res.add(int(p[:i]) * int(p[i:j]))

print sum(res)

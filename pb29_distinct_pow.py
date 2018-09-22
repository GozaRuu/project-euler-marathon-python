#!/usr/bin/env python

#ez but not enough for HackerRank
n = 100
s = set()
for i in xrange(2, n+1):
    for j in xrange(2, n+1):
        s.add(i**j)
print len(s)

# Still didn't figure out a solution for HackerRank for this problem to be honest
# Will update this file when I firgure it out

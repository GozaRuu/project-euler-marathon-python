#!/usr/bin/env python

names = []

def valn(name):
    return reduce(lambda x,y:x+y, map(lambda x:ord(x) - ord('A') + 1, name), 0)

#copying data from the file provided by Project Euler
with open("pb22_names.txt") as f:
    lines = f.readlines()
    names = map(lambda x:x[1:-1], lines[0].strip().split(','))

#reading from HackerRank
# t = int(raw_input().strip())
# for _ in xrange(t):
#     name = raw_input().strip()
#     names.append(name)
# names.sort()
# q = int(raw_input().strip())
# for _ in xrange(q):
#     name = raw_input().strip()
#     print valn(name) * (names.index(name)+1)

res = 0
names.sort()
for i in xrange(len(names)):
    res += valn(names[i]) * (i+1)

print res

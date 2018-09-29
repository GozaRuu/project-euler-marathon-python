#!/usr/bin/env python
from Euler import is_palindrom, str_base

#nice problem, I had to write 2 extra library-worthy function that I added to Euler.py
#in order to solve the HackerRank version

# n, k = map(int, raw_input().strip().split(' ')) #hackerRank
n,k = 10**6, 2

res = 0
for i in xrange(n+1):
    if is_palindrom(str(i)):
        if is_palindrom(str_base(i, ''.join([str(num) for num in xrange(k)]))):
            res += i
print res

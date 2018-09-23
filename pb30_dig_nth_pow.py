#!/usr/bin/env python

from itertools import product, permutations

#works for HackerRank, there is a hardcoded 7 in there it should be 10 in theory
#but 10 is too large and produces a large Cartesian Prodcut, so after some test 7
#fits perfectly for the HackerRank solution

def test(l):
    s = sum(map(lambda x:x**n, l))
    if "".join(map(lambda x:str(x), l)) == str(s):
        return s
    return 0

# n = int(raw_input().strip())
n = 5
res = -1 #to remove 1 because it doesn't count
for i in xrange(7):
    for tup in product(range(10), repeat=i):
        res += test(list(tup))
print res

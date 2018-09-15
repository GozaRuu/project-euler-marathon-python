#!/usr/bin/env python

from Euler import prime_sieve
from bisect import bisect_right

primes = prime_sieve(2000000)
print reduce(lambda x,y:x+y, primes, 0)

#my awesome solution for the HackerRank version of the problem using caching and binary search in additio to the sieve
def HackerRankSol():
    primes = prime_sieve(1000100)
    sum_primes = [0]
    for i in range(1,len(primes)+1):
        sum_primes.append(sum_primes[i-1] + primes[i-1])

    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print sum_primes[bisect_right(primes,n)]

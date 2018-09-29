#!/usr/bin/env python
from bisect import bisect_left
from Euler import prime_sieve

#ez with our prime_sieve and some binary search for hackerRank

primes = prime_sieve(10000000)

def is_circular(n):
    rt_n = str(n)
    for _ in xrange(len(rt_n) -1):
        rt_n = rt_n[-1] + rt_n[:-1] #rotate string
        rt = int(rt_n)
        if primes[bisect_left(primes, rt)] != rt : return False #binary search the answer , primes is already sorted
    return True

# n = int(raw_input().strip())
n = 10**6
n_indx = bisect_left(primes, n)
res = 0
for prime in primes[:n_indx]:
    # if is_circular(prime): res += prime #hackerRank
    if is_circular(prime): res +=1
print res

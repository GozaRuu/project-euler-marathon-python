#!/usr/bin/env python

from Euler import prime_sieve

primes = prime_sieve(2000000)
print reduce(lambda x,y:x+y, primes, 0)

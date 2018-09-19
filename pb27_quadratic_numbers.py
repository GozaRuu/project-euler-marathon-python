#!/usr/bin/env python
from Euler import is_prime, prime_sieve
from bisect import bisect_left

#solution1: ez bruteforce

def sol_1():
    def formula(i,j,k):
        return k**2 + i*k + j

    max_primes, resI, resJ = 0, 0, 0
    for i in xrange(-1000, 1000):
        for j in xrange(i, 1000):
            k = 0
            while is_prime(formula(i, j, k)): k +=1
            if k-1 > max_primes:
                max_primes = k-1
                resI, resJ = i, j


    print resI*resJ

sol_1() #this solves PE

#solution2 much faster with usin the seieve to create all primes needed once
# then binary searching the element to find out if it's prime or not

def sol_2():
    primes = prime_sieve(100000)

    def is_prime_2(n):
        if primes[bisect_left(primes, n)] == n : return True
        return False

    def formula(i,j,k):
        return k**2 + i*k + j

    n = int(raw_input().strip())

    max_primes, resI, resJ = 0, 0, 0
    for i in xrange(-n, n):
        for j in xrange(i, n):
            k = 0
            while is_prime_2(formula(i, j, k)): k +=1
            if k-1 > max_primes:
                max_primes = k-1
                resI, resJ = i, j


    print resI, resJ #this solves all the HackerRank test cases

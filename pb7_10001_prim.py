#!/usr/bin/env python

#solution_1 brute force correct but SLOW for large numbers and multiple requests
def sol_1():
    def is_prime(n):
        if n % 2 == 0 : return False
        i = 3
        while i**2 <= n+1:
            if n % i == 0 : return False
            i += 2
        return True

    def ans(n):
        if n == 1 : return 2
        if n == 2 : return 3
        cpt = 2 ; res = 4
        while cpt < n :
            res += 1
            if is_prime(res) :  cpt += 1
        return res

    print ans(10001)

sol_1()

# cach all primes in an array in case of multiple requests like in the HackerRank version of the problem
def sol_2():
    primes = []
    def is_prime(n):
        if n == 2 or n == 3 : return True
        if n % 2 == 0 : return False
        i = 3
        while i**2 <= n+1:
            if n % i == 0 : return False
            i += 2
        return True

    def get_primes():
        for i in xrange(1000001):
            if is_prime(i): primes.append(i)
    get_primes()
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        print primes[n]

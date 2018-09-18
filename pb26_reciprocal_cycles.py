#!/usr/bin/env python

from Euler import prime_sieve

#this is an application of well known Fermat Permality test that comes from the
#Little theory of Fermat, the idea is that for a prime number p: 1/p produce
#an infinite cycle of length n if 10**(n) - 1 mod p = 0 (this condition triggers just once)
#there is an edge case for primes that divde 10 (2 and 5) so we return 3 for n<7
#IMORTANT: theory from Wikipedia (https://oeis.org/A001913):
#to make a smooth algorithm : Primes p such that the decimal expansion
#of 1/p has period p-1, which is the greatest period possible for any integer

def ans(n):
    if n < 7: return 3
    primes = prime_sieve(n)
    for p in primes[::-1]:
        i = 1
        # while 10**i % p != 1: i += 1
        while pow(10, i, p) != 1: i += 1 #this solves HackerRank constraints, spent a long time on this
        if p - 1 == i : return p #this is the Number Theory trick: Fermat Little theory
# print ans(10000)
print ans(1000)

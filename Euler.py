#!/usr/bin/env python

#ulitmate is_prime function
def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    f = 5
    while f <= int(n**0.5)+1:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


#Calculate gcd
def gcd(a, b):
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    while b != 0:
        a, b = b, a%b
    return a

#Calculate lcm
def lcm(a,b):
    return a*b // gcd(a,b)

#generate prime with the classic sieve  by Robert William Hanks 2010 source: http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
#Very fast (n<10,000,000) in 0.4 sec.

def prime_sieve(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

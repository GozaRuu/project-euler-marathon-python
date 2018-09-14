#!/usr/bin/env python

#fastest solution using euclidian gcd and lcm

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

def lcm(a, b):
    return a*b // gcd(a,b)


print reduce(lambda x,y:lcm(x,y), [x for x in range(1,21)], 1)

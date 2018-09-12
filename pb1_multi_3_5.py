#!/usr/bin/env python

#solution_1

def sol_1():
    return sum ([i for i in range(1000) if i%3 == 0 or i%5 == 0])

print sol_1()

#solution_2 fastest (gaussian sum)

def gauss(n, c):
    n //= c
    return c * n * (n + 1)  // 2

def sol_2(n):
    return gauss(n, 3) + gauss(n, 5) - gauss(n, 15)

print sol_2(999)

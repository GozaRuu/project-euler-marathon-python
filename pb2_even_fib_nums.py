#!/usr/bin/env python

#solution_1

def sol_1():
    fib1 = 1
    fib2 = 1
    res = 0
    while(fib2 < 4000000):
        if(fib2 % 2 == 0): res += fib2
        n = fib1 + fib2
        fib1 = fib2
        fib2 = n
    return res

print sol_1()

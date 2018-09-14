#!/usr/bin/env python

#solution_1 basically a brute force, correct but very slow for multiple request based on an upperbound number

from bisect import bisect_left


def sol_1():
    def plindrom(s):
        if s == s[::-1] : return True
        return False

    res = 0
    for i in reversed(xrange(100,1000)):
        for j in reversed(xrange(100,1000)):
            if len(str(i*j)) == 6 and plindrom(str(i*j)):
                res = max(res, i*j)
    print res


#solution_2 cashing all palindroms in an array, sorting it and, binary-searching the lower_bound using bissect_left

def sol_2():
    arr = []
    for i in range(999,100,-1):
        for j in range(999,100,-1):
            t = str(i*j)
            if t == t[::-1]:
                arr.append(i*j)
    arr.sort()
    print arr[ bisect_left(arr,999999) - 1 ]

sol_2()

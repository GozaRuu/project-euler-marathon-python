#!/usr/bin/env python

#solution_1 brute force O(N**2) correct but SLOW for large numbers and multiple requests
def sol_1():
    n = 1000
    a = 0
    res = -1
    while a<n:
        a += 1
        b = 0
        while b<a:
            b += 1
            if a**2 + b**2 == (n - b - a)**2 :
                res = max(res, a * b * (n - b - a))
    print res


#solution_2 O(N/2) much faster (write b with a and c to get rid of it as a loop)
def sol_2():
    n = 1000
    a = 1 ; c = 0
    res = -1
    while a < n/2:
        if (n**2 % (2 * (n - a)) == 0) and ((c*(n-c)**2 - c**3) % 2 == 0):
            c = (n**2 / (2 * (n - a))) - a
            abc = (c*(n-c)**2 - c**3)/2
            res = max(res, abc)
        a += 1
    print res

#solution3 O(N) same as sol2 but writter with a generator

sol_2()

#!/usr/bin/env python

#solution_1 personal solution using dynamic programming with a recursive function to calculate the
#items in the series and cash them in memo and then fetch the max

def sol_1():
    memo = {1:0}

    def collaz(n):
        if n not in memo: memo[n] = 1 + collaz(n//2) if n % 2 == 0 else 1 + collaz(3 * n + 1)
        #print "memo[", n, "]= ", memo[n]
        return memo[n]


    n = 1000000
    long_chain = 0 ; i = 0
    for i in xrange(1,n+1):
        if collaz(i) >= long_chain :
            long_chain = collaz(i)
            res = i
    print res

sol_1()

#solution 2: quick hack, my original solution times out on huge test cases in HackRank,
#after a quick research it turns out collaz sequence is famous and these list solve the problem

c = [1, 2, 3, 6, 7, 9, 18, 19, 25, 27, 54, 55, 73, 97, 129, 171, 231, 235, 313, 327, 649, 654,
     655, 667, 703, 871, 1161, 2223, 2322, 2323, 2463, 2919, 3711, 6171, 10971, 13255, 17647,
     17673, 23529, 26623, 34239, 35497, 35655, 52527, 77031, 106239, 142587, 156159, 216367,
     230631, 410011, 511935, 626331, 837799, 1117065, 1126015, 1501353, 1564063, 1723519,
     2298025, 3064033, 3542887, 3732423, 5649499, 6649279, 8400511, 11200681]

def sol_2():
    t = int(raw_input().strip())
    for _ in xrange(t):
        n = int(raw_input().strip())
        print min(c[::-1], key=lambda x: x>n)

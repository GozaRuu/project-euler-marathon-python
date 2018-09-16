#!/usr/bin/env python

#solution_1 yet another dynamic programming solution with a recursive function, pretty fast with O(N**2)

memo = [[-1] * 550 for i in xrange(551)]

def ans(n, m):
    if n == 1: return m+1
    if m == 1: return n+1
    #if memo[n][m] == -1: memo[n][m] = ans(n-1, m) % 1000000007 + ans(n, m-1) % 1000000007 use this for HackRank
    if memo[n][m] == -1: memo[n][m] = ans(n-1, m) + ans(n, m-1)
    return memo[n][m]

# HackerRank solution
# t = int(raw_input().strip())
# for i in xrange(t):
#     n,m = map(int, raw_input().strip().split(" "))
#     print ans(n,m) % 1000000007

print ans(20,20)

#!/usr/bin/env python

#A+ problem !!!
#great Dynamic Programming problem especially the HackerRank version with extreme boundries
#This wiki page explains the core idea that I implemented here after experimenting with a bunch of bad ideas
#http://www.algorithmist.com/index.php/Coin_Change

mod = 10**9 + 7
coins = [1, 2, 5, 10, 20, 50, 100, 200]
memo = [[-1 for i in xrange(8)] for j in xrange(100005)]
for i in xrange(8):
    memo[0][i] = 1

def ans(n,m):
    if memo[n][m] == -1:
        memo[n][m] = 0
        if m > 0: memo[n][m] += ans(n, m-1)
        if n >= coins[m]: memo[n][m] += ans(n-coins[m], m)
    return memo[n][m] % mod


#HackerRank
# t = int(raw_input().strip())
# for i in xrange(t):
#     n = int(raw_input().strip())
#     print ans(n,7)

print ans(200,7)

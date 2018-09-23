#!/usr/bin/env python

#A+ problem !!!
#great Dynamic Programming problem especially the HackerRank version with extreme boundries
#This wiki page explains the core idea that I implemented here after experimenting with a bunch of bad ideas
#http://www.algorithmist.com/index.php/Coin_Change

mod = 10**9 + 7
coins = [1, 2, 5, 10, 20, 50, 100, 200]
memo = [[-1 for i in xrange(8)] for j in xrange(10**5 + 1)]

def ans(n,m):
    if n == 0: return 1
    if m == 0: return 1 #if coins[0] != 1 return n % coins[0] == 0 ? 1:0
    if memo[n][m] == -1:
        memo[n][m] = 0
        for coin_index in reversed(xrange(0,m+1)): #use reversed array to take the biggest coin first to avoid going deeper than the maximum recursive calls limit when you start by 1
            if n >= coins[coin_index]: memo[n][m] += ans(n-coins[coin_index], coin_index) % mod
    return memo[n][m] % mod


#HackerRank
# t = int(raw_input().strip())
# for i in xrange(t):
#     n = int(raw_input().strip())
#     print ans(n,7)

print ans(200,7)

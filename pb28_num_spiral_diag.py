#!/usr/bin/env python

#ez brute force over a pattern
def sol_1():
    n = 1001
    ans = [1]
    for i in xrange(3, n+1, 2):
        ans.append(ans[-1] + i**2 + i**2 - (i - 1) + i**2 - 2*(i - 1) + i**2 - 3*(i - 1))

    print ans[-1]

#HackerRank has 10**18 * 10**5 limit !!!! solution need to be O(1) so we use the
#first solution to cach a list for the HackerRank solution with modding

#for this an O(1) we just use the mathematic sum formulas, just add a sum to the
#previous formula and use sum(1,2..n) = n*(n-1)/2 and sum(1,2**2,3**2,...,n**2) =
#n * (n + 1) * (2*n + 1)  // 6 already added those to Euler.py for the future
mod = 10 ** 9 + 7
def HackerRank_solution(n):
    m = (n-1)/2
    s = ((16*(m**3)+26*m)//3)+((10*(m**2))+1)
    return s % mod

print HackerRank_solution(1001)

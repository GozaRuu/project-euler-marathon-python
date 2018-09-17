#!/usr/bin/env python
from math import factorial
from itertools import permutations as perm

#solution 1 very straight forward and easy to write but incredibly slow (of course
#it doesn't solve HackerRank)
def solution_1():
    print ''.join(list(perm('0123456789',10))[999999])


#solution 2
#very nice problem, the idea is baiscally to divide the provided number by
#consecutive factorial numbers use the number as an offset to get the caracter
#and repeat the process with the remeinder as the number and a sliced array

def ans(n, s):
   if len(s) == 1 : return s
   q, r = divmod(n, factorial(len(s) - 1))
   return s[q] + ans(r, s[:q] + s[q + 1:])

n = 1000000
print ans(n-1, '0123456789')
# print perm(n-1, 'abcdefghijklm') HackerRank

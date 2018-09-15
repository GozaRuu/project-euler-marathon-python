#!/usr/bin/env python

div_limit = 42000 #number big enough to cover the HackerRank constraints
n = 500

def ans(n):
	d = [0] * div_limit
	for i in xrange(1, div_limit):
		for j in xrange(i, div_limit, i):
			d[j]+= 1 #add 1 to every multiple of i
		c = d[i-1] * d[i//2] if i % 2 == 0 else d[(i-1)//2] * d[i] #sum the divisors from the array using gauss formula, d[i] or d[i-1] is even for sure
		if c > n: return i*(i-1)//2 #return the triangle number using gauss formula



print ans(n)

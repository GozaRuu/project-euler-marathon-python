#!/usr/bin/env python

# code to generate the amicable numbers array b, we can cash the result and get
#an ultra fast solution O(1) for HackerRank
# b = [0] * 1000005

# for i in xrange(1,len(b)):
#     for j in xrange(2*i,len(b),i):
#         b[j] += i

d = [220, 284, 1184, 1210, 2620, 2924, 5020, 5564, 6232, 6368, 10744, 10856,
 12285, 14595, 17296, 18416, 63020, 66928, 66992, 67095, 69615, 71145, 76084,
  79750, 87633, 88730]


res = 0
n = 10000
for i in xrange(len(d)):
    if d[i] < n: res += d[i]
print res

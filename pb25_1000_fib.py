#!/usr/bin/env python

#ez python ez life
a, b, res = 1, 1, 2
while len(str(b)) < 1000: a, b = b, a+b ; res+=1
print res

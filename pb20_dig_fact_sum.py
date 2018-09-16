#!/usr/bin/env python

import math

#ez python ez life

n = 100
f = math.factorial(n)
print reduce(lambda x,y:x+y, map(int,str(f)), 0)

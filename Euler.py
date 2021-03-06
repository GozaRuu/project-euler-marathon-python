#!/usr/bin/env python

#ulitmate is_prime function
def is_prime(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n % 2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    f = 5
    while f <= int(n**0.5)+1:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True


#Calculate gcd
def gcd(a, b):
    if a < 0:  a = -a
    if b < 0:  b = -b
    if a == 0: return b
    while b != 0:
        a, b = b, a%b
    return a

#Calculate lcm
def lcm(a,b):
    return a*b // gcd(a,b)

#generate prime with the classic sieve  by Robert William Hanks 2010 source: http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
#Very fast (n<10,000,000) in 0.4 sec.
def prime_sieve(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

#sum of multiples of m less than or equal n (generilazation of Gauss fomula)
def gauss(n, m):
    n //= m
    return m * n * (n + 1)  // 2

#sum i**2 i in 1, 2..n
def sum_squares(n):
    return n * (n + 1) * (2*n + 1)  // 6

#sum i**3 i in 1, 2..n
def sum_cubes(n):
    return n**2 * (n + 1)**2  // 4

#write an int in base 10 in a different base, base is a string constructed
#by the characters you need in your base ( eg. base 2: '01', base 8: '01234567', custom base: 'helwivgf')
def str_base(number, base):
    (d,m) = divmod(number,len(base))
    if d > 0: return str_base(d,base) + base[m]
    return base[m]


#checks if integer n is a palindrom
def is_palindrom(n):
    n = str(n)
    m = len(n)//2
    if len(n) % 2 == 0:
        n_1 = n[:m]
        n_2 = n[m:]
        if n_1 == n_2[::-1] : return True
    else :
        n_1 = n[:m]
        n_2 = n[m+1:]
        if n_1 == n_2[::-1] : return True
    return False

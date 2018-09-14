#!/usr/bin/env python

#solution_1

def sol_1():
    primes = []

    def is_prime(x):
        if x == 2 or x == 3: return True
        if x % 2 == 0 or x < 2: return False
        for i in xrange(3, int(x**0.5) + 1, 2):
            if x % i == 0 :
                return False
        return True

    def get_primes():
        for x in xrange(1000000):
            if is_prime(x):
                primes.append(x)


    get_primes()

    # you can manually cach the primes in a file and copy them in the primes variable for a max speed
    # f= open("primes.txt","w+")
    # f.write(','.join([str(x) for x in primes]))
    # f.close()

    for i in reversed(primes):
        if 600851475143 % i == 0 :
            print i
            break

#solution_2 faster than the first solution ( if used without manual cashing of primes)
def sol_2():
    def ans(x):
        while x % 2 == 0 :
                x = x // 2
        if x == 1 :
            return 2

        for i in range(3, int(x**0.5)+1, 2):
            while x % i == 0 :
                x = x // i
            if x == 1 :
                return i
        return x

    print ans(600851475143)

sol_2()

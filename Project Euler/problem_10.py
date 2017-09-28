from math import ceil, sqrt

def isprime(n):
    for x in range(2,ceil(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def sum_primes(n):
    num = 2
    total = 2
    while num < n:
        num += 1
        if isprime(num):
            total += num
    return total


print(sum_primes(2000000))

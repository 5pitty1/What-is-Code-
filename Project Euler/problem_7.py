from math import ceil, sqrt

def isprime(n):
    for x in range(2,ceil(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

def nth_prime(n):
    count = 1
    num = 2
    while count < n:
        num += 1
        if isprime(num):
            count += 1
    return num


print(nth_prime(10001))

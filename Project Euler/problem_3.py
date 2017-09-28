from math import sqrt, floor

def isprime(n):
    for x in range(2, floor(sqrt(n))+1):
        if n % x == 0:
            return False
    return True

N = 600851475143
factor = 2
while factor < N:
    if N % factor == 0:
        print(N // factor)
        if isprime(N // factor):
            break
    factor += 1

print(N // factor)

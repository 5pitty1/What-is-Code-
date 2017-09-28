from math import sqrt, floor

def num_factors(n):
    count = 0
    for x in range(2,floor(sqrt(n))+1):
        if n % x == 0:
            count += 1
    count *= 2
    return count + 2

num = 0
count = 0

while num_factors(num) < 500:
    count += 1
    num += count

print(num)

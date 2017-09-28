from math import sqrt

def triplet_sum(n):
    for x in range(1, n):
        for y in range(x, n):
            if x + y + sqrt(x**2 + y**2) == n:
                return x*y*sqrt(x**2 + y**2)
    return None

print(triplet_sum(1000))

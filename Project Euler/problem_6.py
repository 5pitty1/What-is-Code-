def sum_squares(n):
    total = 0
    for x in range(1,n+1):
        total += x**2
    return total

def square_sums(n):
    total = 0
    for x in range(1,n+1):
        total += x
    return total**2

print(square_sums(100) - sum_squares(100))

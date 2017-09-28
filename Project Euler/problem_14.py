def collatz_length(n):
    count = 1
    while n != 1:
        count += 1
        n = 3*n+1 if n%2 else n//2
    return count

def biggest_collatz(n):
    biggest = (0,0)
    for x in range(1,n):
        biggest = max(biggest, (x, collatz_length(x)), key=lambda x:x[1])
    return biggest

print(biggest_collatz(1000000))

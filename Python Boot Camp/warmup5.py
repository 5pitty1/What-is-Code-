def twoCount(N):
    count = 0
    while N % 2 == 0:
        count += 1
        N /= 2
    return count

print(twoCount(100))

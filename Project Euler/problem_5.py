N = 20

def isDivisible(N):
    for x in range(1,21):
        if N % x:
            return False
    return True

while not isDivisible(N):
    N += 20

print(N)

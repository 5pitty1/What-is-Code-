def solution(i):
    curr = 2
    startingPoint = 0

    while i != 0:
        if isPrime(curr):
            numDigits = countDigits(curr)
            
            if i < numDigits:
                startingPoint = i
                break
            i -= numDigits
        curr += 1

    idString = ""
    print curr
    print startingPoint

    while len(idString) - startingPoint < 5:
        if isPrime(curr):
            idString += str(curr)
        curr += 1

    return idString[startingPoint : startingPoint + 5]


def isPrime(n):
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def countDigits(n):
    count = 0
    while n != 0:
        count += 1
        n = n // 10

    return count


# 23571113171923
print(solution(47))

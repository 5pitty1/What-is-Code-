def is_palindrome(N):
    return str(N) == str(N)[::-1]

biggest = 0
for x in range(999, 99, -1):
    for y in range(999, 99, -1):
        if is_palindrome(x*y):
            biggest = max(x * y, biggest)

print(biggest)

total = 0
current = 2
prev = 1
while current <= 4000000:
    total += current if current % 2 == 0 else 0
    current += prev
    prev = current - prev

print(total)

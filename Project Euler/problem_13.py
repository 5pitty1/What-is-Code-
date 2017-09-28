with open("problem_13.txt") as f:
    total = 0
    for line in f:
        total += int(line)

print(str(total)[0:10])

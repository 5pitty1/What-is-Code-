from itertools import product
from pprint import pprint


def generate(goal):
    H = len(goal) + 1
    W = len(goal[0]) + 1
    permutations = [
        [list(i[x : x + W]) for x in range(0, len(i), W)]
        for i in product("01", repeat=W * H)
    ]
    for i in range(len(permutations)):
        for j in range(len(permutations[0])):
            for k in range(len(permutations[0][0])):
                permutations[i][j][k] = int(permutations[i][j][k])

    count = 0
    for matrix in permutations:
        if isValid(matrix, goal):
            count += 1
            # printMatrix(matrix)

    print(count)


def isValid(curr, goal):
    for i in range(len(goal)):
        for j in range(len(goal[0])):
            target = goal[i][j]
            actual = curr[i][j] + curr[i + 1][j] + curr[i][j + 1] + curr[i + 1][j + 1]
            if target == 1 and actual != 1:
                return False
            if target == 0 and actual == 1:
                return False

    return True


def printMatrix(matrix):
    for row in matrix:
        print(" ".join("0" if x == 1 else "." for x in row))

    print()


x = [
    [list(i[x : x + 2]) for x in range(0, len(i), 2)]
    for i in product("01", repeat=2 * 2)
]

for i in range(len(x)):
    for j in range(len(x[0])):
        for k in range(len(x[0][0])):
            x[i][j][k] = int(x[i][j][k])


for special in x:
    generate(special)
    printMatrix(special)

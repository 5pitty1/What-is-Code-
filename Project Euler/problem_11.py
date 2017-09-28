from operator import mul
from functools import reduce

def load_grid():
    grid = []
    with open("problem_11.txt") as f:
        for line in f:
            splitup = line.split(" ")
            grid.append([int(i) for i in splitup])
    return grid

def check_vectors(n):
    vectors = [(0,1), (1,0), (1,1), (1,-1)]
    biggest = 0
    for vector in vectors:
        for x in range(len(n)):
            for y in range(len(n[0])):
                try:
                    nums = [grid[x + vector[0]*i][y + vector[1]*i] for i in range(4)]
                    biggest = max(biggest, reduce(mul, nums))
                except:
                    pass
    return biggest

grid = load_grid()
print(check_vectors(grid))

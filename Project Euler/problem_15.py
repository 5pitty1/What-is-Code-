
def make_grid(n):
    grid = [[0 for y in range(n+1)] for x in range(n+1)]
    for i in range(n):
        grid[i][n] = 1
        grid[n][i] = 1
    return grid

def lattice_paths(grid):
    for i in range(len(grid)-2, -1, -1):
        for j in range(len(grid)-2, -1, -1):
            grid[i][j] = grid[i+1][j] + grid[i][j+1]

grid = make_grid(20)
lattice_paths(grid)
print(grid[0][0])
# def lattice_paths(grid,x,y):
#     try:
#         if grid[x][y] == 1:
#             return 1
#     except:
#         return 0
#     return lattice_paths(grid, x+1, y) + lattice_paths(grid, x, y+1)
#
#
# grid = make_grid(21)
# print(lattice_paths(grid,0,0))

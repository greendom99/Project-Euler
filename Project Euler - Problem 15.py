grid = []
grid_size = 20

for i in range(1, grid_size+2):
    grid.append([0]*(grid_size+1))
grid[grid_size][grid_size] = 1

# Dynamic Programming
# iterate over positive gradient diagonals starting in bottom right corner working backwards.
for i in range(0, 2*grid_size+1):
    for j in range(0, i+1):
        x = grid_size-j
        y = grid_size*2 - (grid_size-j) - i
        if x == grid_size and y == grid_size:
            continue
        elif x >= 0 and y >= 0:
            if x == grid_size:
                grid[x][y] += grid[x][y+1]
            elif y == grid_size:
                grid[x][y] += grid[x+1][y]
            else:
                grid[x][y] += grid[x][y+1] + grid[x+1][y]
print(grid[0][0])
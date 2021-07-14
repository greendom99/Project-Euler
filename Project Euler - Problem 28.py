# assume always odd
grid_size = 1001

grid = []
for k in range(1, grid_size+1):
    row = [0]*grid_size
    grid.append(row)

# start at centre
(x, y) = (int(grid_size/2), int(grid_size/2))
grid[x][y] = 1

# construct grid by spiralling outwards from centre
count = 2
for i in range(1, grid_size):
    for direction in ['x_direction', 'y_direction']:
        if direction == 'y_direction':
            for j in range(1, i+1):
                x -= (-1)**i
                grid[x][y] = count
                count += 1
        else:
            for k in range(1, i+1):
                y -= (-1)**i
                grid[x][y] = count
                count += 1

for index in range(1, grid_size):
    grid[0][index] = count
    count += 1

diag_sum = 0
for integer in range(0, grid_size):
    diag_sum += grid[integer][integer] + grid[grid_size-1-integer][integer]

# double count centre
diag_sum -= 1
print(diag_sum)

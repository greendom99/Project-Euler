file = open("project_files\\problem_81.txt", 'r')

grid = []
for row in file:
    row = row.split(',')
    row = [int(x) for x in row]
    grid.append(row)

def print_grid(my_grid):
    for row_in_grid in my_grid:
        print(row_in_grid)


size = len(grid)-1
def dynamic_search(optimise):
    for i in range(1, 2*size + 1):
        print("\n\n")
        for j in range(0, i+1):
            x = size - j
            y = size - (i-j)
            if x >= 0 and y >= 0:
                if x == size and y != size:
                    grid[x][y] += grid[x][y + 1]
                elif x != size and y == size:
                    grid[x][y] += grid[x+1][y]
                else:
                    if optimise == 'min':
                        grid[x][y] += min(grid[x+1][y], grid[x][y+1])
                    else:
                        grid[x][y] += max(grid[x + 1][y], grid[x][y + 1])
    return grid[0][0]


print(dynamic_search('min'))

file = open("project_files\\problem_18.txt", "r")

grid = []

for line in file:
    x = line.split(" ")
    x[-1] = x[-1].replace("\n", "")
    x = list(map(int, x))
    grid.append(x)

num_rows = len(grid)

for i in range(num_rows-2,-1,-1):
    for j in range(0,len(grid[i])):
        grid[i][j] = max(grid[i][j]+ grid[i+1][j], grid[i][j]+ grid[i+1][j+1])


print(grid[0][0])
file = open("project_files\\problem_67.txt", "r")

grid = []
for row in file:
    a = row.replace("\n", "")
    a = a.split(" ")
    a = [int(i) for i in a]
    grid.append(a)

for i in range(1, len(grid)):
    a = grid[-(i+1)]
    for index in range(0, len(a)):
        a[index] = max(a[index] + grid[-i][index], a[index] + grid[-i][index+1])

print(grid[0][0])

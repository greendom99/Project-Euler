file = open("project_files\\problem_11.txt", "r")

grid = []

for line in file:
    a = line.split(" ")
    a[-1] = a[-1].replace("\n", "")
    a = [int(i) for i in a]
    grid.append(a)
    grid_size = len(a)


adj_num = 4

# horizontal search
great_prod = 0
for i in range(0, grid_size):
    for j in range(0, grid_size-adj_num+1):
        prod = 1
        for n in range(0, adj_num):
            prod = prod * grid[i][j+n]
        if prod > great_prod:
            great_prod = prod

# vertical search
for j in range(0, grid_size):
    for i in range(0, grid_size-adj_num+1):
        prod = 1
        for n in range(0, adj_num):
            prod = prod * grid[i + n][j]
        if prod > great_prod:
            great_prod = prod


# diagonal search
for i in range(0, grid_size-adj_num+1):
    for j in range(0, grid_size-adj_num+1):
        for z in [1, -1]:
            prod = 1
            for n in range(0, adj_num):
                prod = prod * grid[i+n][j + n*z]
            if prod > great_prod:
                great_prod = prod

print(great_prod)

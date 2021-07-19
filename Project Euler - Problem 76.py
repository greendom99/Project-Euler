target = 100

list_integers = []
for i in range(1, target+1):
    list_integers.append(i)

calc_list = [0]*(target+1)
calc_list[0] = 1

# dynamic programming, adaptation of Problem 31
for integer in list_integers:
    for i in range(0, len(calc_list)):
        if i - integer >= 0:
            calc_list[i] += calc_list[i-integer]
print(calc_list[-1]-1)

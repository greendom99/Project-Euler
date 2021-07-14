coins = [1, 2, 5, 10, 20, 50, 100, 200]

target = 200

calc_list = [0]*(target+1)
calc_list[0] = 1

# dynamic programming
for coin in coins:
    for i in range(0, len(calc_list)):
        if i - coin >= 0:
            calc_list[i] += calc_list[i-coin]
print(calc_list[-1])

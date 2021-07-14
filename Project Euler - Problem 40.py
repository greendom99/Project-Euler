max_power_ten = 6

powers_ten_list = []
for i in range(0, max_power_ten+1):
    powers_ten_list.append(10**i)


def find_product():
    product = 1
    d = 0
    for integer in range(1, powers_ten_list[-1]):
        for digit in str(integer):
            d += 1
            if d in powers_ten_list:
                product = product * int(digit)
                if d == powers_ten_list[-1]:
                    return product


print(find_product())

import math


def check_prime(number):
    if number < 2:
        return False
    for integer in range(2, round(math.sqrt(number)) + 1):
        if number % integer == 0:
            return False
    return True


def search():
    start_size = 1
    diagonal_entry = []
    count = 1

    for size in range(start_size, start_size + 1000000, 2):
        for i in range(size + 1, size + 3, 2):
            for j in range(0, 4):
                count += i
                # j=3 term always a square number
                if j != 3:
                    if check_prime(count):
                        diagonal_entry.append(count)
        if len(diagonal_entry) / (2*size + 3) < 0.1:
            return size+2


print(search())

collatz_lengths = [0] * 1000000


def collatz_sequence(number):
    count = 1
    while number != 1:
        count += 1
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = 3 * number + 1

        # check if already found length for new number
        if collatz_lengths[i - 1] != 0:
            count += collatz_lengths[i - 1]
            number = 1

    return count


for i in range(1, 1000001):
    if collatz_lengths[i - 1] == 0:
        collatz_lengths[i - 1] = collatz_sequence(i)


print(collatz_lengths.index(max(collatz_lengths))+1)

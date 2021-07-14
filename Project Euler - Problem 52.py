def number_to_list(m):
    digits = []
    for digit in str(m):
        digits.append(int(digit))
    return digits


def search(max_lim):
    for n in range(2, 1000000000):
        count = 1

        z = 0
        while z == 0:
            list_digits_x = []
            for i in range(1, max_lim+1):
                m = n * i
                if i == 1:
                    list_digits_x = number_to_list(m).copy()
                    list_digits_x = list(dict.fromkeys(list_digits_x))
                    list_digits_x.sort()
                else:
                    list_digits_ix = number_to_list(m).copy()
                    list_digits_ix = list(dict.fromkeys(list_digits_ix))
                    list_digits_ix.sort()

                    if list_digits_x == list_digits_ix:
                        count += 1
                        if count == max_lim:
                            return n
                        else:
                            continue
                    else:
                        z = 1
                        break


number = search(6)
print(number)

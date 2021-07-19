def sum_digits(a):
    answer = 0
    for digit in str(a):
        answer += int(digit)
    return(answer)


def search():
    max_sum = 0
    for a in range(1, 100):
        print(a)
        for b in range(1, 100):
            term_sum = sum_digits(a**b)
            if term_sum > max_sum:
                max_sum = term_sum
    return max_sum


print(search())

def check_pan(number):
    digits = []
    check_digits = []
    for value, digit in enumerate(str(number)):
        digits.append(value + 1)
        check_digits.append(int(digit))
    check_digits = list(dict.fromkeys(check_digits))
    check_digits.sort()
    if check_digits == digits:
        return True
    else:
        return False


max_found = 0
for value in range(1, 1000000):
    for n in range(1, 1000000):
        num = ''
        for i in range(1, n + 1):
            num += str(i * value)
        if int(num) > 1000000000:
            break

        elif check_pan(int(num)) and len(num) == 9:
            if int(num) > max_found:
                max_found = int(num)
print(max_found)

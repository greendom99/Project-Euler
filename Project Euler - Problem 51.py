import math

def check_prime(number):
    if number < 2:
        return False
    for j in range(2, round(math.sqrt(number)) + 1):
        if number % j == 0:
            return False
    return True


def create_binary_list(m):
    # if digit is 1, we change it, otherwise unchanged
    binary_list = []
    for k in range(0, 2 ** m):
        binary_number = str("{0:b}".format(k)).zfill(m)
        binary_list.append(binary_number)
    # remove trivial no change
    binary_list.pop(0)
    return binary_list


def search():
    for number in list_primes:
        # store the digits of the number in a list
        number_digit_list = []
        num_str = str(number)
        for digit in num_str:
            number_digit_list.append(digit)

        # create list of all binary numbers with same number of digits as number
        # 0 will be unchanged digit, 1 will be changed
        bin_list = create_binary_list(len(str(number)))

        for binary in bin_list:
            digits = []
            for digit in binary:
                digits.append(digit)

            found_prime = []
            count_prime = 0
            for i in range(0, 10):
                replace_number_digit_list = number_digit_list.copy()

                # cant changed leading digit in original number to a 0
                if digits[0] == '1' and i == 0:
                    continue
                else:
                    for index, digit in enumerate(digits):
                        if digit == '1':
                            replace_number_digit_list[index] = str(i)

                new_number = ''
                for digit in replace_number_digit_list:
                    new_number += digit
                new_number = int(new_number)

                if check_prime(new_number):
                    count_prime += 1
                    found_prime.append(new_number)

            if count_prime == 8:
                return found_prime


list_primes = []
for integer in range(2, 1000000):
    if check_prime(integer):
        list_primes.append(integer)


answer_prime = search()
print(answer_prime[0])

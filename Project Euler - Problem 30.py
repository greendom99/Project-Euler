def sum_digits_power(n, power):
    digit_sum = 0
    for digit in str(n):
        digit_sum += (int(digit) ** power)
    return digit_sum


list_numbers = []

for number in range(1, 1000000):
    if number == sum_digits_power(number, 5) and number != 1:
        list_numbers.append(number)

sum_numbers = 0
for num in list_numbers:
    sum_numbers += num
print(sum_numbers)

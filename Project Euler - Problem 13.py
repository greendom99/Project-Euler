file = open("project_files\\problem 13.txt", "r")

list_numbers = []

for line in file:
    number = int(line.replace('\n', ''))
    list_numbers.append(number)

total_sum = 0
for number in list_numbers:
    total_sum += number

first_ten_digits = ''
for i in range(0, 10):
    first_ten_digits = first_ten_digits + str(total_sum)[i]
print(first_ten_digits)

f = open("project_files\\problem_8.txt", "r")

string_number = ''
for line in f:
    edit_line = line.replace('\n', '')
    string_number = string_number + edit_line

number_adj_digits = 13
length_number = len(string_number)

greatest_product = 0
greatest_digits = []

for i in range(0, length_number - number_adj_digits+1):
    digits = []
    product = 1
    for j in range(0, number_adj_digits):
        digits.append(string_number[i+j])
        product = product * int(string_number[i+j])

    if product > greatest_product:
        greatest_product = product
        greatest_digits = digits

print(greatest_product)
print(greatest_digits)

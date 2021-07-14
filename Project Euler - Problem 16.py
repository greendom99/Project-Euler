number = 1000

value = 2 ** number
sum = 0
for digit in str(value):
    sum += int(digit)
print(sum)
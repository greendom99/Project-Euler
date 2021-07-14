from num2words import num2words

max_number = 1000
count = 0
for num in range(1,max_number+1):
    for letter in num2words(num):
        if letter != ' ' and letter != '-':
            count += 1
print(count)

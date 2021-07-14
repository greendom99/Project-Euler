import string

file = open("project_files\\problem_22.txt","r")

for contents in file:
    contents = contents.replace('"', "")
    names = contents.split(",")

names.sort()

letter_values = {}

for value, letter in enumerate(string.ascii_uppercase):
    letter_values[letter]=value+1

total_sum = 0
for value, name in enumerate(names):
    word_sum =0
    for letter in name:
        word_sum += letter_values[letter]
    total_sum += word_sum * (value + 1)

print(total_sum)
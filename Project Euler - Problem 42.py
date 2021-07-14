# import string library function
import string

alphabet = string.ascii_uppercase
letter_value = {}
for count, letter in enumerate(alphabet):
    letter_value[letter] = count + 1

file = open("project_files\\problem_42.txt", "r")


# takes file and returns list of words, formatted nicely
word_list = []
for entry in file:
    word_list = entry.split(',')
for count, word in enumerate(word_list):
    word_list[count] = word.replace('"', '')

# computes word value for each word and stores result in a list
word_value_list = []
for word in word_list:
    word_value=0
    for letter in word:
        word_value += letter_value[letter]
    word_value_list.append(word_value)


# computes relevant triangle numbers
def construct_triangle_list():
    triangle_num_list = []
    for n in range(1, 100000):
        t_n = int(0.5 * n * (n+1))
        if t_n <= max(word_value_list):
            triangle_num_list.append(t_n)
        else:
            return triangle_num_list

def count_triangle_words():
    i = 0
    triangle_numbers = construct_triangle_list()
    for value in word_value_list:
        if value in triangle_numbers:
            i += 1
    return i


print(count_triangle_words())

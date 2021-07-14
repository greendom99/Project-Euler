def check_palindrome_base_ten(number):
    if str(number) == str(number)[::-1]:
        return True
    else:
        return False

def check_palindrome_base_2(number):
    binary = "{0:b}".format(number)
    if str(binary) == str(binary)[::-1]:
        return True
    else:
        return False


answer_sum = 0
for i in range(1, 1000000):
    if check_palindrome_base_ten(i):
        if check_palindrome_base_2(i):
            answer_sum += i
print(answer_sum)
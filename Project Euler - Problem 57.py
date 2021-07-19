numerator = 1
denominator = 2
count = 0
for i in range(0, 1000):
    if i == 0:
        numerator = 1
        denominator = 2
        answer_numerator = numerator + denominator
    else:
        old_numerator = numerator
        numerator = denominator
        denominator = 2*denominator + old_numerator
        answer_numerator = denominator + numerator

    if len(str(answer_numerator)) > len(str(denominator)):
        count += 1
print(count)


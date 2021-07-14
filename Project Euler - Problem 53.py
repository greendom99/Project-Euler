def factorial(m):
    product = 1
    if m != 0:
        for i in range(1, m+1):
            product = product * i
    return product

def n_choose_r(j, k):
    value = factorial(j)/(factorial(k)*factorial(j-k))
    return int(value)

def search():
    count = 0
    for n in range(1, 101):
        for r in range(0, n+1):
            if n_choose_r(n, r) > 1000000:
                count += 1
    return count


answer = search()
print(answer)

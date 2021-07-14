max_number_sol = 0
p_max = 0

for p in range(3, 1000):
    number_sol = 0
    for a in range(1, p+1):
        for b in range(a, (p-a) // 2 + 1):
            c = p - a - b
            if a**2 + b**2 == c**2:
                number_sol += 1
    if number_sol > max_number_sol:
        max_number_sol = number_sol
        p_max = p
print(p_max)
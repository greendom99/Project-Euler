values = []
for a in range(2,101):
    for b in range(2,101):
        values.append(a**b)
values.sort()
values = list(dict.fromkeys(values))
print(len(values))

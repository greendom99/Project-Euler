import itertools

num_count = 9

num_list = []
for n in range(0,num_count+1):
    num_list.append(n)

perm_list = list(itertools.permutations(num_list))

answer = ''
for b in perm_list[1000000-1]:
    answer += str(b)
print(int(answer))

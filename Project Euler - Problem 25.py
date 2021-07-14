fib_seq = [1, 1]

while len(str(fib_seq[-1]))<1000:
    fib_seq.append(fib_seq[-1]+fib_seq[-2])
print(len(fib_seq))
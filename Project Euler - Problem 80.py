from decimal import Decimal, localcontext

master_sum = 0
for i in range(1, 101):
    x = i ** 0.5
    if x.is_integer():
        continue
    else:
        with localcontext() as ctx:
            ctx.prec = 102
            sqrt_i = str(Decimal(i).sqrt())
            term_sum = 0
            for digit in str(sqrt_i)[:101]:
                if digit != '.':
                    term_sum += int(digit)
            master_sum += term_sum
print(master_sum)

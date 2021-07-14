def search():
    n = 286
    m = 166
    k = 144

    while True:
        t_n = n * (n + 1) // 2
        p_n = m * (m * 3 - 1) // 2
        h_n = k * (k * 2 - 1)
        minimum = min(t_n, p_n, h_n)
        if minimum == max(t_n, p_n, h_n):
            return str(t_n)

        if minimum == t_n:
            n += 1
        if minimum == p_n:
            m += 1
        if minimum == h_n:
            k += 1


print(search())


import math


def check_perfect_square(number):
    if int(math.sqrt(number) + 0.5) ** 2 == number:
        return True
    else:
        return False

def check_integer(number):
    if int(number + 0.5) == number:
        return True
    else:
        return False


# number theory approach
def search():
    for k in range(2, 10000000):
        for l in range(1, k):
            x = 1 + 6 * (k-l)*(3*(k+l)-1)
            y = 1 + 6 * (3*(k**2 + l**2)-k-l)
            if check_perfect_square(x) and check_perfect_square(y):
                if check_integer(1/6 * (int(math.sqrt(x))+1)) and check_integer(1/6 * (int(math.sqrt(y))+1)):
                    m = int(1/6 * (int(math.sqrt(x))+1))
                    n = int(1/6 * (int(math.sqrt(y))+1))
                    dif = int(0.5*n*(3*n - 1) - 0.5*m*(3*m - 1))
                    return dif


print(search())

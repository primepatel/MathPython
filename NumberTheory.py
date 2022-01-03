def is_odd(number):
    return number%2 == 1


def is_even(number):
    return number%2 == 0

def gcd_loop(m, n=1):
    if n == 1:
        return abs(m)
    while m%n != 0:
        m, n = n%m, m
    return abs(n)
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

def gcd_recursive(m, n):
    m, n = abs(m), abs(n)
    if n == 0:
        return m
    else:
        return gcd_recursive(n, m%n)

# Test gcd_loop vs gcd_recursive

def gcd_multi(*args):
    gcd = args[0]
    for i in args[1:]:
        gcd = gcd_loop(gcd, i)
    return gcd
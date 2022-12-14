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


def eea(m, n):
    a0, a1, b0, b1 = 1, 0, 0, 1
    while n != 0:
        m, n, q = n, m%n, m//n
        a0, a1, b0, b1 = b0, b1, a0 - q*b0, a1 - q*b1
    return m, a0, a1


def gcd_multi(*args):
    gcd = args[0]
    for i in args[1:]:
        gcd = gcd_loop(gcd, i)
    return gcd

def is_coprime(a, b):
    if gcd_loop(a, b) == 1:
        return True
    else:
        return False

def lcm_loop(m, n = 1):
    return abs(m*n)//gcd_loop(m, n)

def lcm_multi(*args):
    lcm, n = args[0], args[0]
    for i in args[1:]:
        lcm = lcm_loop(lcm, i)
    return lcm

def factorization(number):
    """try using prime generators
    function used in phi function where factorization returns dictionary"""
    factors = {}
    while number != 1:
        for i in range(2, number+1):
            if number % i == 0 :
                number //= i
                if i in factors:
                    factors[i] += 1
                    break
                factors[i] = 1
                break
    return factors

# print(factorization(25))

def euler_phi(number):
    for i in factorization(number):
        number = number*(i-1)//i
    return number


def is_prime(number):
    if number <= 1:
        return False
    elif number == 2:
        return True
    else:
        if number%2 == 0:
            return False
        for i in range(3, int(number**0.5)+1, 2):
            if number%i == 0:
                return False
        return True

def is_composite(number):
    return not is_prime(number)


class Num_pow:
    def __init__(self, number, power = 1) -> None:
        self.number = number
        self.power = power

    def __mod__(self, n):
        """used euler's theorem"""
        return (self.number ** (self.power % euler_phi(n))) % n

# print(Num_pow(123, 345)%5, (123**345) % 5)

def primes(m):
    yield 2
    m -= 1
    P, n = [2], 3
    while m != 0:
        for i in P:
            if n%i == 0:
                break
        else:
            m -= 1
            yield n
            P.append(n)
        n += 2

# for i in primes(10):
#     print(i)

def prime(index):
    if index == 1:
        return 2
    P = [2]
    index -= 1
    n = 3
    p = 2
    while index != 0:
        for i in P:
            if n%i == 0:
                break
        else:
            p = n
            index -= 1
            P.append(n)
        n += 2
    return p

# print(prime(12))

def prime_less_than(n):
    if n < 2:
        yield None
    else:
        yield 2
        P = [2]
        p = 3
        while p<=n:
            for i in P:
                if p%i == 0:
                    break
            else:
                yield p
                P.append(p)            
            p += 2

# for i in prime_less_than(29):
#     print(i)

class G_Int:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
        self.norm = a*a + b*b
    def is_gprime(self):
        if is_prime(self.norm):
            return True
        print(self.norm)
        factors = factorization(self.norm)
        print(factors)
        k_v = tuple(factors.items())[0]
        print(k_v)
        if len(factors) == 1:
            if factors[k_v[0]] == 2 and k_v[1]%4 == 3:
                return True
        return False


# print(G_Int(3, 2).is_gprime())
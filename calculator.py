# https://github.com/PaulK1246/lab10-YK-KZ.git
# Partner 1: Yechan Kim
# Partner 2: Kellen Zander


import math

def square_root(a):
    try:
        if a < 0:
            raise ValueError
        return math.sqrt(a)
    except TypeError:
        raise ValueError

def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b):
    return a + b


def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def logarithm(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid arguments for logarithm.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b


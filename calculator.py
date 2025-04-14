# https://github.com/PaulK1246/lab10-YK-KZ.git
# Partner 1: Yechan Kim
# Partner 2: Kellen Zander

import math

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

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError
    return math.log(b, a)

def exp(a, b):
    return a ** b

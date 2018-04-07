from random import random


def print_me(n=456, s="default-value"):
    """this function prints the stupid inputs"""
    print(f"The first input is {n}")
    print(f"The second input is {s}")
    return "you are dumb"


def estimate_pi(n=1000):
    inside = 0
    for i in range(n):
        r1 = random() - 0.5
        r2 = random() - 0.5
        r = (r1 ** 2 + r2 ** 2) ** 0.5
        if r < 1/2:
            inside += 1
    print(inside)
    return float(inside) * 4 / n


print_me.__doc__    # return the thing in triple ""
total = 0


def f():
    global total
    total += 1
    return total


def add(a, b):
    return a + b


def func(a, b, fu=add):
    return fu(a, b)


def outer():
    var = 'sac'

    def inner():
        nonlocal var
        print(var)

    inner()


# Returning global variables in functions
# var = estimate_pi(1000000)
# print_me(s="aisehi")
# We should have all the default params in the end as python assign values in order
# parameters are variables in our function def
# arguments are values with which we call our function
# passing method names as params
# using global variables in method requires special work

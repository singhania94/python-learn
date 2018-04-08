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


print_me.__doc__                            # return the thing in triple ""
total = 0


def using_global_var():                    # using global variables in method requires special work
    global total
    total += 1
    return total


def add(a, b):
    return a + b


def func_param_pass(a, b, fu=add):      # func name can also be passed as arguments
    return fu(a, b)


def outer():
    var = 'sac'

    def inner():
        nonlocal var        # required if you want to use an outside variable
        print(var)

    inner()


def what_does_pass_do():         # does nothing
    pass


def star_args(*args):       # args is a tuple containing any arbitrary args passed
    print(args)             # star_args(123, 'Meryl Streep', True)
    pass                    # tu = (123, True, "Marry her");  star_args(*tu)


def star_star_args(**kwargs):      # intakes all arguments as dictionary
    print(kwargs)                   # star_star_args(dat='12th',married=True)
    pass                            # di = {'name':'Aditya', 'surname':'Singahnia'};  star_star_args(**di)

# Returning global variables in functions
# We should have all the default params in the end as python assign values in order
# parameters are variables in our function def
# arguments are values with which we call our function
# Ordering
#   1. params
#   2. *args
#   3. params with default values
#   4. **kwargs

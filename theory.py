import sys

# REPL stands for Read evaluate Print Loop commands on console
# Executes a file instead of interpreting

# print("Variable value is ", var, ", you idiot")
# print(f"Variable value is {var * 89}, you idiot")
# print("Variable value is {}".format(26))

# snake_case for variables
# CAP_SNAKE_CASE for constants
# UpperCamelCase for classes
# __underscore__ no touch variables

var = ''
type(var)           # prints type of variable

# check if values are equal ==
# check if both reference same location 'is'.
# also, x is 1,'any-string' if x=1,'any-string' will return true
# '', None, 0 always return false

# from random import randint
# from random import choice

# Parameter ordering
# func(params, *args, default_params, **kwargs)

i = [134, 1341, 134, 12]

# All returns if all are True
# all(list comprehension) can also be used
all(i)

# Any return if at least one is True
any(i)
sys.getsizeof(i)     # return size of the object
# sorted(i, key=lambda u: u['username'], reverse=False)
reversed(i)     # returns a reversed iterator
# max(i, key=lambda u: len(u['username']))      # instead of an iterable list, generator expr obj can also be passed.
min(i)
len(i)  # calls __len__() method, we can implement for ourselves
abs(234)
# sum(iterable, start)
round(1.2352352454, 2)      # nearest integer if digits not specified
# zip(iterable1, iterable2) forms a tuple of pairs of i'th of both iterable
# zip (*iterable) does the opposite of what a zip does to an iterable

m = [80, 93, 76]
f = [104, 64, 75]
s = ['dan', 'ang', 'kate']
var = {v[0]: max(v[1], v[2]) for v in zip(s, m, f)}
var = dict(                 # other way of doing it
    zip(
        s,
        map(
            lambda p: max(p),
            zip(m, f)
        )
    )
)

print(var)
print(list(zip(var, m)))
print(list(zip(*var.keys())))

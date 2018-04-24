# higher order functions
def outer_func(st):
    def inner_func():
        return st
    return inner_func


a_func = outer_func("aisehi")
# print(a_func())


def outside(ins):
    def wrapper():
        print('do something')
        ins()
        print('do another something')
    return wrapper


@outside
def inside():
    print('welcome to the core')


# outside(inside)() without @ is same as
# inside() now basically,     inside = outside(inside) is declared automatically
# @ is calling the outside method basically with inside function as a param


from functools import wraps


def standard_func(f):
    @wraps(f)           # preserves the metadata of the function f
    def wrapper(*args, **kwargs):
        return f(*args, **kwargs).upper()
    return wrapper


@standard_func
def greet():
    return "hello"

# print(greet());


def passing_args(val):
    def inner_func(fn):
        def wrapper(*args, **kwargs):
            print(f'from a wrapper {val}')
            print(fn(*args, **kwargs))
            print('done')
        return wrapper
    return inner_func


# What is actually happening, demo = passing_args('aisehi')(demo)
@passing_args('aisehi')
def demo():
    return 'hello'


demo()






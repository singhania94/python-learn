# REPL stands for Read evaluate Print Loop commands on console
# Executes a file instead of interpreting

var = 9
# print("Variable value is ", var, ", you idiot")
# print(f"Variable value is {var * 89}, you idiot")
# print("Variable value is {}".format(26))
var2 = 7.0
var = float(7)
type(var)           # prints type of variable
var**var2           # Exponentiation
var = var//var2     # Integer division
var = "tomorrow"

# snake_case for variables
# CAP_SNAKE_CASE for constants
# UpperCamelCase for classes
# __underscore__ no touch variables

# bool, int, str, list, dict{JSON}
var = True
var = [2, 3, True, "wow"*3]*2
var = None
type(var)
var = {
    "name": "aditya",
    "profession": ["tomorrow", 56],
    "address": {
        "plot": "New RadhaKisan plots"
    }
}

# "" '' both can be used to declare strings
var = " " + "tomorrow".lower()
var[2]
var[-2]
var[var.__len__()-1]
var = str(9)
# var = input("Enter a variable:")
var = 7.74986824596
round(var, 2)       # round 2 decimal points

# Conditions Boolean expressions

# if condition:
#    doSomething
# elif otherCondition:
#    doSomething
# else:
#    goNuts

# check if values are equal ==
# check if both reference same location 'is'. Also, x is 1,'any-string' if x=1,'any-string' will return true
# '', None, 0 return false
# == != < > <= >= conditional-operators 'and' 'or' 'not'

# from random import randint
# from random import choice

# for var in iterable/range(start, stop):
#   doSomething
# range(num) 0->num-1
# range(num1, num2) num1->num2-1
# range(n1, n2, n3) n3 denotes steps

# while condition:
#   doSomething
# break


# Lists
var = ['tomatoes', 'american-hustle', 'airplanes']*6
var.__len__()
len(var)
var.append(['toronto', 'tomorrow'])     # to add just this as an object to list
var.extend([34, 35])    # to expand the list
# var.sort()
# var.insert(3, '235')
# var.clear()
# var.pop(2)
# var.remove('value')     # remove the first occurance
# var.count('value')      # count of occurances of the value
# var.index('value')     # returns the index of value
# var.reverse()
# var = list(range(1, 10))
# var[2]
# var[-1]
# var[3:]     # slices the list now starting at 3 index
# var[3:6]    # slices upto the mentioned end but one
# var[::]     # step index
# var[3], var[5] = var[7], var[3]     # swapping values
# var = [x*7 for x in var if x % 2 == 0]            # [operation for x in var] returns a new modified list
#  here 'if' can be appended anywhere
var = "Python rocks, Java shockzz!"
# print(''.join([v for v in var if v not in "aeiou"]))    # removing vowels from string
# [ x if x==0 else x-1 for x in list]       # if else occuring in the start for optional values
var = [[1, 2, 3], [5, 6, 7], [10, 22]]  # nested list
# [[print(i) for i in l] for l in var]
# 45 in var                   # returns if it contains the object
# "var-string".join(var)      # joins the list appending the string in between
# var = range(20)
# var.__contains__('')
# print(type(var))
var = dict(name="kitty", age=56)
var = {
    "item": "gel-pen",
    "quantity": 3,
    "price": 56.98,
    "is_eatable": False,
    4: 78947389
}
var["item"]
var.keys()
var.values()
var.items()

# for key, value in var.items():




print(var)


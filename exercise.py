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
var = " " + "tomorrow"
var[2]
var[-2]
var[var.__len__()-1]
var = str(9)
# var = input()
var = 7.74986824596
round(var, 2)       # round 2 decimal points
print(var)


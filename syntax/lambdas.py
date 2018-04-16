squared_lambda = lambda num: num ** 2  # anonymous function stored in a variable
add_lambda = lambda a, b: a + b  # used to pass across; one liner short functions
# instead of creating function definitions

i = [32423, 343, 2343423, 43]
users = [{"name": 'John', 'surname': "Maxwell"},
         {"name": "Aditya"},
         {"name": "Timothy", "surname": "Granger"}]

# Maps double = map(function/lambda, iterable)
# doubles is a map object which can only be iterated over once
var = map(lambda n: n ** 2, i)

# Filter filters out the items returning false values
# returns a filter object
var = (filter(lambda v: v == 56), i)

var = list(map(lambda u: u['name'].upper(),
               filter(lambda u: not u['name'][0] == 'a', users)))
var = [u['name'].upper() for u in users if not u['name'][0] == 'a']
# Generator expression object if [] not specified in comprehension. Good if you want to iterate once.
# These can be achieved by list comprehension as well


print(var)

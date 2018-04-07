# tuple is immutable list
var = (324, 23423, 32432)
var = tuple(['today', 'tomorrow'])
# iterate, count, index, slicing, cutting, nested-tuples same as lists

# sets is a list with unique elements
# no rigid order
var = {1, 2, 3, 4, 5}
var = set({1, 2, 3, 4, 5, 5, 5})
87 in var
# access values via for loop
var.add(34)
var.remove(3)
var.discard("Moscow")       # does'nt throw KeyError
var.copy()
var.clear()
# intersection, sym_diff, union of sets can be done
var1 = {343, 2324, 234, 2342}
var2 = {423, 343, 23432, 32}
var1 & var2
var1 | var2
var = {x**2 for x in range(100)}

print(var)

# 1. SyntaxError : syntax is wrong
# 2. NameError : variable has not been defined
# 3. TypeError : Mismatch of data types, number of args in function
# 4. IndexError : index access that does not exist
# 5. ValueError : Expected a different value but is invalid as per the operation eg. convert_to_int("foo")
# 6. KeyError : Dictionary does not have the specified key
# 7. ZeroDivisionError :
# 8. AttributeError : Variable does'nt have attribute

# Custom errors
# raise TypeError('this is a message')    # optional message

# Handle errors
try:
    print('something' + 5)
except TypeError as err:            # TypeError can be replaced with Error
    print(err)
else:                               # runs if error does'nt occur
    print('Everything fine')
finally:                            # Runs anyways
    print("I'm done")

# PDB python debugger
var = [1343, 'Aditya', 'Singhania']
print('before')
# import pdb; pdb.set_trace()         # l - list, n - next, p - print, c - continue
print('after')

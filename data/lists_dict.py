var = [2, 3, True, "wow"*3]*2
var = ['tomatoes', 'american-hustle', 'airplanes']*6
len(var)
var.append(['toronto', 'tomorrow'])     # to add just this as an object to list
var.extend([2, 34, 35])    # to expand the list
# var.sort()
var.insert(3, '235')
# var.clear()
var.pop(2)
# var.remove('value')     # remove the first occurance
var.count('value')      # count of occurances of the value
# var.index('value')     # returns the index of value
var.reverse()
var = list(range(1, 10))
var[2]
var[-1]
var[3:]     # slices the list now starting at 3 index
var[3:6]    # slices upto the mentioned end but one
var[::]     # step index
var[3], var[5] = var[7], var[3]     # swapping values
# here 'if' can be appended anywhere but has a different meaning at both places
var = "Python rocks, Java shockzz!"
# print(''.join([v for v in var if v not in "aeiou"]))    # removing vowels from string
# var = [x*7 for x in var if x % 2 == 0]     # [operation for x in var] returns a new modified list
# [[print(i) for i in l] for l in var]
# [x if x == 0 else x-1 for x in list]       # if else occuring in the start for optional values
# var = [[1, 2, 3], [5, 6, 7], [10, 22]]  # nested list
# 45 in var                   # returns if it contains the object
"var-string".join(var)      # joins the list appending the string in between
var = range(20)
var.__contains__('')

var = {
    "name": "aditya",
    "profession": ["tomorrow", 56],
    "address": {
        "plot": "New RadhaKisan plots"
    }
}

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
# lists cannot be used as keys
# for key, value in var.items():
"item" in var   # returns if the key is present
# if var["item"]:
#    print("var contains item");
3 in var.values()      # searches in values
var.clear()
var2 = var.copy()
var = {}.fromkeys(["key"], "value")
var = dict.fromkeys(["key1"], "value")
var2 = var.fromkeys(["key"], "value")
var = {}.fromkeys(["key1", "key2", "key3"], "value")
# var["key"]          # throws exception if does'nt exist
var.get("key")      # return None if does'nt exist
# var.pop("key")      # removes key-value pair, throws error
var.popitem()       # removes a item at random
var.update(var2)    # updates, adds var with var2
# {final_key: final_value for k,v in var.items()}   # iterates over keys by default
# [card(k, v) for k in keys for v in values]    iterates over all combination of k, v
# conditional logic can also be used using 'if'

# var = dict(l2)    # if l2 is a list of pairs, can be done

print(var)

# read from file
file = open("C:\\Users\\AS66422\\wspace\\git\\python-learn\\resources\\dict.txt")
print(file.read())
file.seek(0)        # moves the cursor to that char
# Cursor - move tool in file, file dynamically loads as the file changes
print(file.readline())
print(file.readlines())      # returns a list of lines after the cursor location
# file.close()
with open("C:\\Users\\AS66422\\wspace\\git\\python-learn\\resources\\dict.txt") as file:
    file.read()
# automatically closes the file, thanks to with
# with calls __enter__(), and at the end calls __exit__()

# write to file
with open("C:\\Users\\AS66422\\wspace\\git\\python-learn\\resources\\dict.txt", 'w') as f:      # default is 'r'
    f.write("Tomorrow is dooms day\n")                                                          # 'a', 'x', 't', 'r+'
    f.write("this is fun")

# CSV files, importing DictReader presents as a dict, import writer to write, DictWriter to write
from csv import reader, DictWriter

with open('C:\\Users\\AS66422\\wspace\\git\\python-learn\\resources\\csv_file.csv') as file:
    csv_reader = reader(file)           # delimitor=','
    for row in csv_reader:
        pass
        # print(row)

with open('C:\\Users\\AS66422\\wspace\\git\\python-learn\\resources\\csv_write_file.csv', 'w') as file:
    headers = ["name", "age", "city"]
    writer = DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerow({
        'name': 'santa',
        'age': 345,
        'city': 'amsterdam'
    })
    writer.writerow({
        'name': 'banta',
        'age': 3434,
        'city': 'amsterdam'
    })
    writer.writerow({
        'name': 'hanta',
        'age': 345,
        'city': 'amsterdam'
    })

# import pickle
# object o = Object()
# with open("pickle_example.pickle", "wb") as file:
#    pickle.dump(o, file)
# with open("pickle_example.pickle", "rb") as file:
#    o = pickle.load("file")

import json

j = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
print(j)
# It formats a python object as a String of json
# o.__dict__ - converts an object to dict representation which can be json.dumps(o.__dict__)

# import jsonpickle
# frozen = jsonpickle.encode(o)
# file.write(frozen)
# jsonpickle.decode(o)

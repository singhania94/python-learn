# Encapsulation - hiding some sensitive data from the user -
# _var - private variable
# __msg - _class__msg
# Abstraction - Hiding the inner working of the class
# self - current instance of the class

class User:
    """
        blueprint for user
    """
    activeUsers = 0         # static variable

    def __init__(self, name='Im', surname='nameless'):
        self.name = name
        self.surname = surname
        self.age = 6372
        User.activeUsers += 1

    def print_user(self):
        print(f"name:{self.name} surname:{self.surname} age:{self.age}")

    def __repr__(self):                             # this gets printed when print(object) is called
        return f"first:{self.name} last:{self.surname}"

    @classmethod
    def from_string(cls, s):
        return User(*s.split(","))

    @classmethod
    def print_class(cls):
        print(f"Class method:{cls}")


user1 = User()
# User.print_class()
# User.from_string("Aditya,Singhania").print_user()


class Car(object):
    """
        blueprint for car
    """

    def __init__(self, model, color, company, speed_limit):
        self.color = color
        self.company = company
        self.speed_limit = speed_limit
        self.model = model

    def start(self):
        print(f"started {self}")


maruti_suzuki = Car("ertiga", "black", "suzuki", 60)
audi = Car("A6", "red", "audi", 80)
# audi.start()


class Animal:

    def __init__(self, name):
        self._age = 0
        self.name = name

    @property
    def age(self):              # allows us to call animal.age
        return self._age

    @age.setter
    def age(self, value):       # allows us to set animal.age = 87, -78
        self._age = max([0, value])

    def make_sound(self, sound):
        print(f'make sound {sound}')

    def do_something(self):
        raise NotImplementedError("Implement this method in child class")

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name)        # Animal.__init__(self, name)
        self.species = species

    def do_something(self):
        pass

# In multiple inheritance the first mentioned class is referred via super and both class
# methods are available but first mentioned class superceeds authority

# MRO method resolution order
# first look in cat, then animal
# __mro__ attribute, mro() method, help(class) provide a look into mro ordering

# Polymorphism
# same method, different classes - method override
# same method, different inputs - method overload - mul(a, b); mul(a, b, c);
# Dander methods - __repr__, __str__, __add__(self, other), __len__, __mul__
# in dictionary, __missing__, __setitem__, __iter__

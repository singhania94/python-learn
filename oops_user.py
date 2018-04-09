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

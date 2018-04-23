import collections
# iterator - object that can be iterated upon, next() method can only be called on iterator
# iterable - object that return iterator iter(object) return iterable
# list, string are examples of iterable
# next() method returns the next item until a StopIteration error occurs


class Counter:
    def __init__(self, lo, hi):
        self.p = 0
        self.current = lo
        self.hi = hi
        super(Counter, self).__init__()

    def __iter__(self):
        return self
#       return iter(range(self.lo, self.hi))

    def __next__(self):
        if self.current < self.hi:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for n in Counter(50, 65):
    print(n)

c = Counter(45, 456)
print(isinstance(c, collections.Iterable))  # True

# Generator - every gen is an iterator, but not vice versa


def count_up_to(num):
    a = 1
    while a <= num:
        yield a
        a += 1


o = count_up_to(5)
# o is a generator object

next(o)     # gives you the next number
# raises StopIterator exception
# all the values are generated as and when called, quite faster
# operation stops at yield, and continues from there the next time

# Generator expressions
g = (ge for ge in range(1, 10))



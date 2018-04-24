# -O ignores all assertions
# assert
def add_positives(x, y):
    assert x > 0 and y > 0, "Both should be positive numbers"
    return x + y


# doctests
# python -m doctest -v file.name
def add_another(x, y):
    """ adds two numbers
    >>> add_another(2,3)
    5
    >>> add_another(200,300)
    500
    >>> add_another('45', 56)
    Traceback (most recent call last):
    ...
    TypeError: must be str, not int
    """
    return x + y


# unittest
import unittest


# run with -v for verbose
class DemoTests(unittest.TestCase):

    def setUp(self):
        print('Before')

    def test_add_positives(self):
        """ testing function add positives"""
        self.assertEqual(add_positives(500, 650), 1150, "They are not equal")
        self.assertEqual(add_positives(500, 650), 1150, "They are not equal")
        self.assertEqual(add_positives(500, 650), 1150, "They are not equal")
        with self.assertRaises(TypeError):
            add_another('34', 56)

    def tearDown(self):
        print('After')


if __name__ == '__main__':
    unittest.main()






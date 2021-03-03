# pyTest for FizzBuzz.py
import unittest
from FizzBuzzImp import *
class CustomTests(unittest.TestCase):
    # compare input is not number type
    def test_runs1(self):
        #array is including 100 arrays
        self.assertTrue(array[2] == "Fizz")
        self.assertTrue(array[5] == "Fizz")
        self.assertTrue(array[8] == "Fizz")
        #array got "Fizz" every #3 array
    # def test_runs2(self):
    #     pass
    # def test_runs3(self):
    #     #array got 19 "Buzz"
    #     pass
if __name__ == '__main__':
    unittest.main()

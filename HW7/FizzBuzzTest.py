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
        #FizzBuzz --> check number print "Fizz" 3 6 9
    def test_runs2(self):
        self.assertTrue(array[4] == "Buzz")
        self.assertTrue(array[9] == "Buzz")
        self.assertTrue(array[19] == "Buzz")
        #array check number print "Buzz" 5 10 20
    def test_runs3(self):

        self.assertTrue(array[14] == "FizzBuzz")
        self.assertTrue(array[29] == "FizzBuzz")
        self.assertTrue(array[44] == "FizzBuzz")
        #array check number print "Buzz" 15 30 45

if __name__ == '__main__':
    unittest.main()

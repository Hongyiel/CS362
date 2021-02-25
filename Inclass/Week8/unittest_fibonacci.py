import unittest
import fibonacci

class TestCaseFibo(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(fibonacci.Fibonacci(10),10)
    def test_case2(self):
        self.assertIsNotNone(fibonacci.Fibonacci(5))
        # get . if Fibonacci's value is exist
    def test_case3(self):
        self.assertIsNone(fibonacci.Fibonacci(0))


class TestCaseFacto(unittest.TestCase):
    def test_case_fact1(self):
        self.assertEqual(fibonacci.Factorial(2),15)
    def test_case_fact3(self):
        self.assertIsNotNone(fibonacci.Factorial(12))
    def test_case_fact2(self):
        self.assertTrue(fibonacci.Factorial(33))




if __name__ == '__main__':
    unittest.main()

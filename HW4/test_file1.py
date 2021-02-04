import unittest
import Problem1
class CustomTests(unittest.TestCase):
    # compare input is not number type
    def test_runs1(self):
        get_test = Problem1.find_cube("char")
        self.assertTrue(type(get_test) is not str)
    # compare input is not over 0
    def test_runs2(self):
        get_test = Problem1.find_cube(3)
        self.assertGreater(get_test, 0)
    # compare input is not None
    def test_runs3(self):
        get_test = Problem1.find_cube(10)
        self.assertIsNone(get_test)
if __name__ == '__main__':
    unittest.main()

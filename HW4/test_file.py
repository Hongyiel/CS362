import unittest
import Problem1
class CustomTests(unittest.TestCase):
    def test_runs1(self):
        get_test = Problem1.find_cube(8)
        self.assertTrue(type(get_test) is not str)
    def test_runs2(self):
        get_test = Problem1.find_cube(-3)
        self.assertGreater(get_test, 0)
    def test_runs3(self):
        get_test = Problem1.find_cube(10)
        self.assertIsNotNone(get_test)
if __name__ == '__main__':
    unittest.main()

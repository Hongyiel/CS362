import unittest
import Problem2
class CustomTests(unittest.TestCase):
    # get list prams are allowed
    def test_runs1(self):
        get_test = Problem2.get_list([2,'c',1])
        self.assertTrue(type(get_test) is not str)
    # Check input exist
    def test_runs2(self):
        get_test = Problem2.get_list([5,6,7])
        self.assertIsNotNone(get_test)
    # Check list type or not
    def test_runs3(self):
        get_test = Problem2.get_list((3,3,3))
        self.assertIsInstance(get_test, list, msg=None)


if __name__ == '__main__':
    unittest.main()

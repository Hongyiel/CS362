import unittest
import Problem3
class CustomTests(unittest.TestCase):
    # get list prams are allowed
    def test_runs1(self):
        # should have String type with first name and last name
        get_test = Problem3.get_name(str,str)
        self.assertTrue(get_test, str)
    def test_runs2(self):
        # should have equal type with first name and last name
        get_test = Problem3.get_name(str,str)
        self.assertEqual(get_test['First_name'], get_test['Last_name'])    # def test_runs3(self):
    def test_runs3(self):
        # Does input type was dict type?
        expected = {}
        get_test = Problem3.get_name(str,str)
        subset = {k:v for k, v in get_test.items() if k in expected}
        self.assertDictEqual(subset, expected)

if __name__ == '__main__':
    unittest.main()

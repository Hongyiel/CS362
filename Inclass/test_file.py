import unittest
import In_class_act

class TestCaseCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(In_class_act.add(10, 1), 11)
    def test_sub(self):
        self.assertEqual(In_class_act.sub(10, 1), 9)
    def test_div(self):
        self.assertIsNotNone(In_class_act.div(10, 0))
        # if got None get error
    def test_mul(self):
        self.assertEqual(In_class_act.mul(10, 1), 10)
if __name__ == '__main__':
    unittest.main()

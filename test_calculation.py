import unittest

import caluculation

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = caluculation.Cal()
        self.assertEqual(cal.add_num_and_dobule(1, 1), 4)


    def test_add_num_and_double_raise(self):
        cal = caluculation.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_dobule('1', '1')

# CLI
if __name__ == '__main__':
    unittest.main()
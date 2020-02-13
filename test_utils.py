# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(4), 24)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1, -2, 1), (1))
        self.assertEqual(utils.roots(1, 1, 1), ())
        self.assertEqual(utils.roots(1, -2, -8), (4, -2))
    
    def test_integrate(self):
        self.assertEquals(utils.integrate("x**2", 0, 2), 8/3)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())

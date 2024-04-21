#test division.py

import unittest
from division import dividir
class TestDividir(unittest.TestCase):
    def test_dividir(self):
        self.assertEqual(dividir(4,2),2)
        self.assertEqual(dividir(-1,1),1)
        self.assertEqual(dividir(-1,-1),1)
        self.assertEqual(dividir(0,2),0)
        self.assertEqual(dividir(2,0),'ZeroDivisionError: division by zero')

if __name__ == '__main__':
    unittest.main()
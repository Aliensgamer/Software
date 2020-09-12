import unittest
from Software import Edad

class TestProblema1(unittest.TestCase): 
    def test_calcularedad(self):
        s=Edad()
        edad=s.calcularedad(20,2020)
        self.assertEqual(edad, 70) 

if __name__ == "__main__":
    unittest.main()
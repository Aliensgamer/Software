import unittest
from Software3 import Palabra

class TestProblema1(unittest.TestCase): 
    def test_calcularP(self):
        s=Palabra()
        palabra=s.Letra("ElectZ")
        self.assertEqual(palabra, ('E', 'Z')) 

if __name__ == "__main__":
    unittest.main()
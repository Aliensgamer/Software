import unittest
from Software2 import Numero

class TestProblema1(unittest.TestCase): 
    def test_calcularN(self):
        s=Numero()
        numero=s.PI(10)
        self.assertTrue(numero)

if __name__ == "__main__":
    unittest.main()
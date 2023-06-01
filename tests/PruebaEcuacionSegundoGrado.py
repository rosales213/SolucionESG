import unittest
from src.logica.EcuacionSegundoGrado import EcuacionSegundoGrado

class PruebaEcuacionSegundoGrado(unittest.TestCase):
    def test_EcuacionSegundoGrado_parametrosNumericos_RaicesReales(self):
        # Arrange
        a = 3
        b = -5
        c = 1

        X1Esperado = 1.43
        X2Esperado = 0.23


        # Do
        ecuacion = EcuacionSegundoGrado()
        X1Actual, X2Actual = ecuacion.calculoECS(a, b, c)

        # Assert
        self.assertEqual(X1Actual, X1Esperado)
        self.assertEqual(X2Actual, X2Esperado) # add assertion here


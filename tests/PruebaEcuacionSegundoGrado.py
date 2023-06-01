import math
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
        precision = math.fabs(X1Esperado - X1Actual)
        self.assertLessEqual(precision, 0.001)
        precision = math.fabs(X2Esperado - X2Actual)
        self.assertLessEqual(precision, 0.001)


    def test_EcuacionSegundoGrado_parametrosNumericosMultiple_RaicesReales(self):
        ecuacion = EcuacionSegundoGrado()
        items = (
            {"Case": "Caso 01", "a": 3, "b": -5, "c": 1, "RaizEsperada1": 1.43, "RaizEsperada2": 0.23},
            {"Case": "Caso 02", "a": 1, "b": 2, "c": 1, "RaizEsperada1": -1.00, "RaizEsperada2": -1.00},
            {"Case": "Caso 03", "a": -1, "b": 2, "c": -1, "RaizEsperada1": 1.00, "RaizEsperada2": 1.00},
            {"Case": "Caso 04", "a": 1, "b": 0, "c": -18, "RaizEsperada1": 4.24, "RaizEsperada2": -4.24},
            {"Case": "Caso 05", "a": 1, "b": 4, "c": 0, "RaizEsperada1": 0.00, "RaizEsperada2": -4.00},
            {"Case": "Caso 06", "a": 1, "b": 4, "c": 4, "RaizEsperada1": -2.00, "RaizEsperada2": -2.00},
            {"Case": "Caso 07", "a": 1, "b": 3, "c": 2, "RaizEsperada1": -1.00, "RaizEsperada2": -2.00},
        )
        # do
        for item in items:
            with self.subTest(item["Case"]):
                RaizActual1, RaizActual2 = ecuacion.calculoEGS(item["a"], item["b"], item["c"])

        #assert
        self.assertEqual(item["RaizEsperada1"], RaizActual1)
        self.assertEqual(item["RaizEsperada2"], RaizActual2)
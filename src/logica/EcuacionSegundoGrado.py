import math
class EcuacionSegundoGrado:
    def calculoEGS(self, a, b, c):
        discriminante = pow(b,2)-4*a*c
        if discriminante >= 0:
            raizdiscriminante = math.sqrt(discriminante)
            X1 = (-b + raizdiscriminante) / (2 * a)
            X2 = (-b - raizdiscriminante) / (2 * a)
        return X1, X2


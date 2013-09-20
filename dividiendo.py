# -*- coding: utf-8 -*-

class Modelo:
    
    divisor = 23

    def devolver_resultado(self, numero):
        """ Divide el número por el diviso y devuelve un entero """
        resultado = numero//self.divisor
        return resultado

    def __init__(self):
        valor = raw_input("Elige un número entero entre 0 y 100: ")
        valor = float(valor)
        resultado = self.devolver_resultado(valor)
        print "%d/%d es %d" % (valor, float(self.divisor), float(resultado))

obj = Modelo()
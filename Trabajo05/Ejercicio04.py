"""
   Ejemplo04
   Generar, imprimira y obtenga el resultado de la serie:
   1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + 1/13 - 1/15
"""

from fractions import Fraction
numerador = 1
contadordenominador = 3
operación = 0
cadenaFinal = ""

cadenaFinal = "%s%d" % (cadenaFinal,numerador)
operación = operación + numerador 

for i in range (1,17,-1):
    if (i % 2) == 0:
        cadenaFinal = "%s + %d/%d" % (cadenaFinal,
        numerador,
        contadordenominador,
        operación)
        operación = operación + float(numerador/contadordenominador)

    else:
        cadenaFinal = "%s - %d/%d" % (cadenaFinal,
        numerador,
        contadordenominador,
        operación)
        operación = operación - float(numerador/contadordenominador)

        contadordenominador = contadordenominador + 2

cadenaFinal = "%s = %.2f" % (cadenaFinal,operación)
print(cadenaFinal)
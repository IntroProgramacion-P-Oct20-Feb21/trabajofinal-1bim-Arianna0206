"""
   Ejemplo03
   Generar e imprimir la siguiente serie:
   2 5 10 17 26 37
"""

contador = 3
contador2 = 1
número = 2
cadenaFinal = ""

while (contador2 <= 5):
    número = número + contador
    contador = contador + 2
    contador2 = contador2 + 1

    cadenaFinal = "%s\t%d" % (cadenaFinal,número)

print(cadenaFinal)



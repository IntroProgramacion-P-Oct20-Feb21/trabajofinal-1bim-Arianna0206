"""
   Ejemplo02
   Generar e imprimir la siguiente serie:
   2 6 12 20 30 42 56 72 90 110
"""

contador = 1
contador2 = 2
contador3 = 1
cadenaFinal = ""

while(contador3 <= 10):
      número = contador * contador2
      
      contador = contador + 1
      contador2 = contador2 + 1
      contador3 = contador3 +1
      
      cadenaFinal = "%s\t%d" % (cadenaFinal,número)

print(cadenaFinal)


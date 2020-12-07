"""
   Ejemplo11
"""

tabla = 10
cadena01 = ""
cadena02 = ""
contador = 1

while(contador <= 5):
    operacion01 = tabla + contador
    operacion02 = tabla * contador
    cadena01 = "%s%d + %d = %d\n" % (cadena01,tabla,contador,operacion01)
    cadena02 = "%s%d * %d = %d\n" % (cadena02,tabla,contador,operacion02)
    contador = contador + 1

print("%s\n%s\n" % (cadena01,cadena02))

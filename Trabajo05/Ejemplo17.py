"""
   Ejemplo17
"""

contador = 1
cadena = ""
operacion = 0

while contador <= 5:
   cadena = ("%sTabla de multiplicación del número: %d\n" % (cadena,contador))

   for i in range(1,10,1)
        operacion = i * contador
        cadena = ("%s%d * %d = %d\n" % (cadena,contador,i,operacion))

    cadena = ("%s\n" % cadena)
    contador = contador + 1

print("%s\n" % cadena)
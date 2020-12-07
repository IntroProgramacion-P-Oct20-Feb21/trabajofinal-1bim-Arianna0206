"""
   Ejemplo16
"""

contador = 1
operacion = 0

tabla = int(input("Ingrese la tabla a generar: "))
while contador <= 10:
    operacion = tabla * contador
    print("%d * %d = %d\n" % (tabla,contador,operacion))
    contador = contador + 1
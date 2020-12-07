"""
   Ejemplo13
"""

cadenaFinal = ""
contador = 1
operacion = 0

numeroTabla = int(input("Ingrese el número de tabla:\n"))
limiteTabla = int(input("Ingrese el limite de tabla:\n"))
print("Introduzca 1 para suma \Introduzzca 3 para multiplicación")
opcion = int(input("Introduzca aqui su opción: "))

if opcion == 1:
    cadenaFinal = ("%s%s\n" % (cadenaFinal, "Tabla de sumar"))
    while contador <= limiteTabla:
        operacion = numeroTabla + contador
        cadenaFinal = ("%s%d + %d = %d\n" % (cadenaFinal,numeroTabla,contador,operacion))
    contador = contador + 1

elif opcion == 2:
    cadenaFinal = ("%s%s\n" % (cadenaFinal, "Tabla de multiplicar"))
    while contador <= limiteTabla:
        operacion = numeroTabla * contador
        cadenaFinal = ("%s%d * %d = %d\n" % (cadenaFinal,numeroTabla,contador,operacion))
    contador = contador + 1

else:
    cadenaFinal = ("%s%s\n" % (cadenaFinal,"Error en tipo de operación"))

print("%s\n" % cadenaFinal)


"""
   Ejemplo14
"""

cadenaFinal = ""
bandera = True
salida = ""

while(bandera):
    nota = float(input("Ingrese calificaciones: "))
    cadenaFinal = ("%s%.2f\n" % (cadenaFinal,nota))

    if salida < 0:
        bandera = False

print("Listado de Notas\n%s\n" % cadenaFinal)

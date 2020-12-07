"""
   Ejemplo13
"""

cadenaFinal = ""
bandera = True
salida = ""

while(bandera):
    notas = float(input("Ingrese calificaciones: "))
    cadenaFinal = ("%s%.2f\n" % (cadenaFinal , notas))

    print("Ingrese (si) si desea salir del ciclo: ")
    if(salida == "si"):
        bandera = False

print("Listado de Notas\n%s\n" % cadenaFinal)
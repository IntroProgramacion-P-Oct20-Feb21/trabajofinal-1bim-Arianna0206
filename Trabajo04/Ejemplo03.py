"""
   Ejemplo08
"""

cadena = str(input("Ingrese el nombre del día de la semana: "))

if (cadena == "Lunes"):
    print("%s\n" % cadena)
elif (cadena == "lunes"):
    print("%s\n" % cadena)
elif (cadena == "Martes"):
    print("%s\n" % cadena) 
elif (cadena == "martes"):
    print("%s\n" % cadena)
elif (cadena == "Jueves"):
    print("%s\n" % cadena)
elif (cadena == "jueves"):
    print("%s\n" % cadena)
else:
    print("Ninguna de las anteriores")
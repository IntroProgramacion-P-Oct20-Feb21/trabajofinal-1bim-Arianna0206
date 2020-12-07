"""
   Ejemplo16
"""

nombre = str(input("Ingrese el nombre del comprador: "))
largo = float(input("Ingrese el largo del terreno: "))
ancho = float(input("Ingrese el ancho del terreno: "))
costoMetro = float(input("Ingrese el costo del m2 del terreno: "))

area = (largo * ancho)
costoTerreno = (area * costoMetro)

print("El costo del terreno es: %.2f\nNombre del comprador: %s" % (costoTerreno,nombreComprador))
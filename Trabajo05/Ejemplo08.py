"""
   Ejemplo12
"""

contador = 1
cadena01 = ""

while(contador <= 5):
    nombre = str(input("Ingrese el nombre del trabajador: "))
    sueldo = float(input("Ingrese el sueldo del trabajador: "))
    ciudad = str(input("Ingrese la ciudad del trabajador: "))

    cadena01 = ("%s (%.2f) -%s-\n" % (nombre,sueldo,ciudad))
    contador = contador + 1

print("%s\n" % cadena01)
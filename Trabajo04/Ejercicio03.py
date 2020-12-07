"""
   Ejemplo03
   Calcular el valor a cancelar por la empresar para cada empleado Presentar un reporte como el siguiente:
   Nombre 1	10	$2.5	$25
   Nombre 2	11	$2	$22
   Nombre 3	9	$3	$27
   Nombre 4	5	$4	$20
   Nombre 5	12	$2	$24
"""

contador = 0
bandera = True
cadenaFinal = ""


 while(bandera):
       nombre = str(input("Ingrese el nombre del empleado: "))
       número = int(input("Ingrese el número de días trabajados: "))
       costo = int(input("Ingrese el costo del día trabajado: "))
       contador = contador +1
       cadenaFinal = " %s%d.) %s \t %d \t$ %2.f\n" % (cadenaFinal, \
                                                      contador,nombre,
                                                      número,costo)
       salir = input("Desea salir del ciclo, ingrese si: ")
       if salir == "si":
           bandera = False

cadenaFinal = "Listado de empleados\n%s" % (cadenaFinal)

print(cadenaFinal) 

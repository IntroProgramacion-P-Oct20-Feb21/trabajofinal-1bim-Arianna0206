"""
   Ejemplo05
   Permita ingresar 4 estudiantes
   Presentar el siguiente reporte
   Estudiante 1	10	Aprobado
   Estudiante 2	6.9	Reprobado
   Estudiante 3	7	Aprobado
   Estudiante 4	5	Reprobado
   Atención; con base al valor del promedio, usted debe asignar en cada registro el tipo Aprobado o Reprobado
"""

contador = 1
cadenaFinal = ""
while(contador <= 4):
    nombre = str(input("Ingrese el nombre del estudiante: "))
    promedio = float(input("Ingrese el promedio del ciclo del estudiante: "))
    if (promedio >= 7.0):
        cadena = "Aprobado"
    else:
        cadena = "Reprobado"
     
    cadenaFinal = "%s%d.) %s \t %d \t %s\n" % (cadenaFinal,\
    contador,nombre,promedio,cadena)
    contador = contador + 1 

cadenaFinal = "Datos de los estudiantes\n%s" % (cadenaFinal)
print(cadenaFinal)


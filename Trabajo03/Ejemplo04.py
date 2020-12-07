"""
   Ejemplo07
"""

promedio = 10

if(promedio >= 7.5):
    print("Estudiante aprobado con un promedio: %.2f\n" % promedio)
else:
    if((promedio >= 5)&(promedio <= 7.4)):
        print("Estudiante en suspenso con un promedio: %.2f\n" % promedio)
    else: 
        print("Estudiante reprobado con un promedio: %.2f\n" % promedio)

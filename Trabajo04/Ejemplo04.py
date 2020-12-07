"""
   Ejemplo09
"""

numeroDia = int(input("Ingrese el número de dís de la semana: "))

if (numeroDia == 1):
    print("Día %d es %s\n" % (numeroDia, "Lunes"))
elif (numeroDia == 2):
    print("Día %d es %s\n" % (numeroDia, "Martes"))
elif (numeroDia == 3):
    print("Día %d es %s\n" % (numeroDia, "Miércoles"))
elif (numeroDia == 4):
    print("Día %d es %s\n" % (numeroDia, "Jueves"))
elif (numeroDia == 5):
    print("Día %d es %s\n" % (numeroDia, "Viernes"))
elif (numeroDia == 6):
    print("Día %d es %s\n" % (numeroDia, "Sábado"))
elif (numeroDia == 7):
    print("Día %d es %s\n" % (numeroDia, "Domingo"))
else:
    print("Opción incorrecta")
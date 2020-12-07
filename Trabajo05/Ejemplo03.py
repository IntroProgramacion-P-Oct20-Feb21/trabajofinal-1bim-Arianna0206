"""
   Ejemplo07
"""
region = ""
mensajeFinal = ""

print("Introduzca 1 para Región Sierra \Introduzca 2 para Región Costa \Introduzzca 3 para Región Amazónica \Introduzca 4 para Región Insular")

opcion = int(input("Introduzca aqui su opción: "))

if(opcion == 1):
    region = "Región Sierra"
    mensajeFinal = ("Usted seleccionó: %s\n" % region)
elif(opcion == 2): 
    region = "Región Costa"
    mensajeFinal = ("Usted seleccionó: %s\n" % region)
elif(opcion == 3):
    region = "Región Amazónica"
    mensajeFinal = ("Usted seleccionó: %s\n" % region)
elif(opcion == 4):
    region = "Región Insular"
    mensajeFinal = ("Usted seleccionó: %s\n" % region)
else:
    print("Error, no existe región")

print(mensajeFinal)
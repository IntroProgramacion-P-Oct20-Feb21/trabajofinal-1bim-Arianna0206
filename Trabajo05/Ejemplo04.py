"""
   Ejemplo08
"""
region = ""
mensajeFinal = ""

print("Introduzca 1 para Región Sierra \Introduzca 2 para Región Costa \Introduzzca 3 para Región Amazónica \Introduzca 4 para Región Insular")

opcion = int(input("Introduzca aqui su opción: "))

if(opcion == 1):
    region = "Región Sierra"
    
elif(opcion == 2): 
    region = "Región Costa"
    
elif(opcion == 3):
    region = "Región Amazónica"
    
elif(opcion == 4):
    region = "Región Insular"
    
else:
    region = "Error, no existe región"

print("Usted seleccionó: %s\n" % region)
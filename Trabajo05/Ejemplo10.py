"""
   Ejemplo14
"""

bandera = True
salir = ""

while(bandera):
    salir = str(input("Desea salir del ciclo; digite: si: "))
    salir = salir.lower()

    if(salir == "si"):
        bandera = False

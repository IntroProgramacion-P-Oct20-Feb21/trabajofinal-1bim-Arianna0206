"""
   Ejemplo04
   Calcular el costo total de una computadora comprada por partes
"""

costo_CPU = float(input("Ingrese el costo del CPU: "))
costo_Teclado = float(input("Ingrese el costo del teclado: "))
costo_Pantalla = float(input("Ingrese el costo de la pantalla: "))
costo_Ratón = float(input("Ingrese el costo del ratón: "))
  
Total = float(costo_CPU)+float(costo_Teclado)+float(costo_Pantalla)+(costo_Ratón)      

print("el costo total de la computadora es: " + str(Total))
        
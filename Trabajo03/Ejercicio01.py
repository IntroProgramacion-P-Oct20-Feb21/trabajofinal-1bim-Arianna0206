"""
   Ejercicio01
   Calcular el valor a cancelar de una planilla de luz
   Si el usuario tiene edad mayor a 65 años, se debe descontrar el 10%
"""

porcentaje = 10
costo = float(input("Ingrese el costo por kilovatio/hora: "))
número = float(input("Ingrese el número de kilovatios consumidos en el mes: "))
edad = int(input("Igrese la edad de la persona: "))

if edad > 65:
   print("Es usted mayor de 65 años por lo tanto si obtiene el descuento")
else:
   print("Es usted menor de 65 años por lo tanto no obtiene el descuento")
 
 valor_Planilla = (float(costo) * float(número))
 descuento = (int(porcentaje) * float(valor_Planilla)/100)
 valor_Planilla = (float(valor_Planilla) - float(descuento))
 

 print("el valor de la planilla es: " + str(valor_Planilla))

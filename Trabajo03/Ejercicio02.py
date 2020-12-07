"""
   Ejercicio02
   Calcular el costo de un pedido de un artículo 
   Si la cantidad pedida excede de 50 unidades, se hace un descuento de 15%
"""

porcentaje = 15
costo = float(input("Ingrese el costo de las unidades: "))
cantidad = float(input("Ingrese en número de unidades: "))

if cantidad > 50:
   print("Usted compró mas de 50 unidades")
else: 
   print("Usted no excedio mas de las 50 unidades")

costoTotal = (float(costo)*float(cantidad))
descuento = (int(porcentaje)*float(costo)/100)
costoTotal = (float(costoTotal)-float(descuento))

print("el costo de un pedido de un artículo es: " + str(costoTotal))
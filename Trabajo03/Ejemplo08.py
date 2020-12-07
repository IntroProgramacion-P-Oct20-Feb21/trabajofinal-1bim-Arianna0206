"""
   Ejemplo11
"""

porcentaje1 = 10
porcentaje2 = 15
porcentaje3 = 20

numeroDias = int(input("Ingrese el número de días que se hospedará"))
precioHabitación = float(input("Ingrese el valor diario de la habitación"))

if(numeroDias > 5 & numeroDias <= 10):
   subtotal = numeroDias * precioHabitación
   descuento = ((porcentaje1 * subtotal)/100)
   valorTotal = subtotal - descuento
else:
    if(numeroDias > 10 & numeroDias <= 15):
        subtotal = numeroDias * precioHabitación
        descuento = ((porcentaje2 * subtotal)/100)
        valorTotal = subtotal - descuento
    else: 
        if(numeroDias > 15):
            subtotal = numeroDias * precioHabitación
            descuento = ((porcentaje3 * subtotal)/100)
            valorTotal = subtotal - descuento 
        else:
            subtotal = numeroDias * precioHabitación
            descuento = 0
            valorTotal = subtotal - descuento

print("El valor subtotal es: %.2f\nEl descuento es: %.2f\nEl valor total a pagar es: %.2f\n" % (subtotal,descuento,valorTotal))
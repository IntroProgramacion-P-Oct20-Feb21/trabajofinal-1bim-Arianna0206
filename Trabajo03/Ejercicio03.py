"""
   Ejercicio03
   Calcular el impuesto por pagar y el precio de venta (incluido el impuesto). Si el origen es Alemania el impuesto es 20%, si es de Japón el impuesto es 30%, si es de Italia, 15%, y si es de USA, 8%
"""

impuesto_Alemania = 20
impuesto_Japón = 30
impuesto_Italia = 15
impuesto_USA = 8

marca = str(input("Ingrese la marca del vehiculo: "))
origen = str(input("Ingrese el origen del vehiculo: ")) 
precio = float(input("Ingrese el precio del vehiculo: "))

if origen == "Alemania":
   impuesto = (int(impuesto_Alemania)*float(precio)/100)
   impuesto_pagar = (impuesto + precio)
else:
    if origen == "Japón":
      impuesto = (int(impuesto_Japón)*float(precio)/100)
      impuesto_pagar = (impuesto + precio)
    else:
        if origen == "Italia":
           impuesto = (int(impuesto_Italia)*float(precio)/100)
           impuesto_pagar = (impuesto + precio)
        else:
            if origen == "USA":
                impuesto = (int(impuesto_USA)*float(precio)/100)
                impuesto_pagar = (impuesto + precio)
            

impuesto_pagar ="El precio de venta es: %.3f\nEl impuesto por pagar es: %.4f\n" % (precio,impuesto_pagar)

print(impuesto_pagar)

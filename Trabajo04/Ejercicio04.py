"""
   Ejercicio04
   Permita ingresar 10 jugadores de baloncesto
   Generar el siguiente reporte
   Jugador 1	100	10
   Jugador 2	200	25
   Jugador 3	99	33
   Jugador 4	80	41
   Jugador 5	60	50
"""

contador = 1
cadenaFinal = ""
while(contador <= 10):
     nombre = str(input("Ingrese el nombre del jugador: "))
     puntos = int(input("Ingrese el número de puntos que anotó en la temporada: "))
     faltas = int(input("Ingrese el número de faltas de la temporada: "))
     cadenaFinal = "%s%d.) %s \t %d \t %d\n" % (cadenaFinal,\
     contador,nombre,puntos,faltas)
     contador = contador + 1

cadenaFinal = "Listado de jugadores\n%s" % (cadenaFinal)
print(cadenaFinal)
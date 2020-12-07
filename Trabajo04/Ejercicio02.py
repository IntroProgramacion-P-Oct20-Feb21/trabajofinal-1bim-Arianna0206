"""
   Ejemplo02
   Presentar en pantalla la siguiente secuencia: 1/10 2/20 3/11 4/21 5/12 6/22
"""

numerador = 1
denominador1 = 20
denominador2 = 10
        while (numerador <= 6):
            if numerador % 2 == 0:
                print("El número %d es par", numerador,"/" ,denominador1)
                denominador1 = denominador1 + 1
            else:
                print("El número %d es impar", numerador, "/" , denominador2)
                denominador2 = denominador2 + 1
             
            numerador = numerador + 1            
            
            
            
#!/usr/bin/python3
"""
Demostrando que si n impar y n>=5
n es congruente con 1 modulo 6 o n es congruente con 5 modulo 6
"""
import math
from termcolor import colored
max = 1000

mensaje = set()
mensaje={True:colored('Aceptado','green'), False:colored('Rechazado','red')}

fichero = open( "resultado.txt","w" )

for num in range(2,max):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
        if (num == 2 or num == 3):
            continue
        print(num)
        print(mensaje[(num%6 == 1%6) or (num%6 == 5%6)])

        fichero.write("\nn = " + str(num))
        fichero.write("\nPrueba n ≡ 1 mod 6 : ")
        fichero.write(str(num) + " modulo 6 = "+str(num%6))
        fichero.write("\t 1 modulo 6 = 1")
        fichero.write("\t :: "+str(num%6 == 1%6))
        fichero.write("\nPrueba n ≡ 5 mod 6 : ")
        fichero.write(str(num) + " modulo 6 = "+str(num%6))
        fichero.write("\t 5 modulo 6 = 5")
        fichero.write("\t :: "+str(num%6 == 5%6))

fichero.close()

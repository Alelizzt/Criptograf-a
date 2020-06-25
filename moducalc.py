#!/usr/bin/python3


# coding: utf-8
import os.path
import pyfiglet
from termcolor import colored

fichero = open( "resultado.txt","w" )

def banner():
    mensaje = pyfiglet.figlet_format("ModuCalc") 
    print(colored(mensaje, 'cyan'))

def sumar(a,b,zn):
    global fichero
    print(colored('Realizando suma ...','green'))
    print('('+ str(a) + '(+)' + str(b) + ') mod ' + str(zn) )
    fichero.write('('+ str(a) + '(+)' + str(b) + ') mod ' + str(zn) + '\n')
    suma = a + b
    print('('+ str(suma) +') mod '+ str(zn) )
    fichero.write('('+ str(suma) +') mod '+ str(zn) + '\n' )
    return suma % zn

def multiplicar(a,b,zn):
    global fichero
    print(colored('Realizando multiplicacion ..','green'))
    print('('+ str(a) + '(x)' + str(b) + ') mod ' + str(zn) )
    fichero.write('('+ str(a) + '(x)' + str(b) + ') mod ' + str(zn) + '\n' )
    multiplicacion = a * b
    print('('+ str(multiplicacion) +') mod '+ str(zn) )
    fichero.write('('+ str(multiplicacion) +') mod '+ str(zn) + '\n' )
    return multiplicacion % zn

def sustraer(a,b,zn):
    global fichero
    print(colored('Realizando sustraccion ...','green'))
    print('('+ str(a) + '(x)' + str(b) + ') mod ' + str(zn) )
    fichero.write('('+ str(a) + '(x)' + str(b) + ') mod ' + str(zn) + '\n')
    sustraccion = a - b
    print('('+ str(sustraccion) +') mod '+ str(zn) )
    fichero.write('('+ str(sustraccion) +') mod '+ str(zn) + '\n')
    return sustraccion % zn

def main():
    global fichero 
    banner()
    zetha_usuario = input('Ingrese Zn: ')
    a_usuario = input('Ingrese el valor de A: ')
    b_usuario = input('Ingrese el valor de B: ')
    
    fichero.write("Zn = " + zetha_usuario + "\n")
    fichero.write("A = " + a_usuario + "\n")
    fichero.write("B = " + b_usuario + "\n")

    try:
        zetha = int(zetha_usuario)
        a = int(a_usuario)
        b = int(b_usuario)
        if (a<0 or b<0 or zetha<0):
            print(colored('[-] Los valores ingresados no pertenecen al conjunto Zn', 'red'))
            fichero.write("Los valores no pertenecen al conjunto Zn" + "\n")
            fichero.close()
            exit(0)
        if (b == 0):
            print(colored('[-] B no puede tener el valor 0'))
            fichero.write("B no puede tener el valor 0" + "\n")
            fichero.close()
            exit(0)
        if (zetha == 0):
            print(colored('[-] Zn no puede ser cero, por la propiedad n-1','red'))
            fichero.write("Zn no puede ser cero, incumple la propiedad limite (n-1)" + "\n")
            fichero.close()
            exit(0)
    except ValueError:
        print(colored('[-] Alguno de los valores ingresados no pertenecen a los numeros enteros','red'))
        fichero.write("Algunos valores no pertenecen al conjunto de numeros enteros" + "\n")
        fichero.close()
        exit(0)

    print ("""
        Seleccione la operacion a realizar
        [1].Suma modular
        [2].Multiplicacion modular
        [3].Sustraccion modular
        """)
    ans=input("Digite la opcion :") 
    if ans == "1": 
        print(colored('[!] ha seleccionado la opcion suma','yellow'))
        resp = sumar(a,b,zetha)
        print(colored('[+] El resultado es: '+ str(resp),'green'))
        fichero.write('El resultado es: '+ str(resp) + "\n")
        fichero.close()
    elif ans == "2":
        print(colored('[!] ha seleccionado la oipcion multiplicacion','yellow'))
        resp = multiplicar(a,b,zetha)
        print(colored('[+] El resultado es: '+ str(resp),'green'))
        fichero.write('El resultado es: '+ str(resp) + "\n")
        fichero.close()
    elif ans == "3":
        print(colored('[!] ha seleccionado la opcion sustraccion','yellow'))
        resp = sustraer(a,b,zetha)
        print(colored('[+] El resultado es: '+ str(resp),'green'))
        fichero.write('El resultado es: '+ str(resp) + "\n")
        fichero.close()
    else:
        print(colored('[-] Opcion incorrecta','red'))
if __name__ == '__main__':
    main()

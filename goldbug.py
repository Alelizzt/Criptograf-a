#!/usr/bin/python3
from termcolor import colored

print(colored('Mensaje cifrado: \n', 'yellow'))

print(" 5 3 ‡ ‡ † 3 0 5 ) ) 6 * ; 4 8 2 6 ) 4 ‡ ")
print(" . ) 4 ‡ ) ; 8 0 6 * ; 4 8 † 8 ¶ 6 0 ) ) ")
print(" 8 5 ; 1 ‡ ( ; : ‡ * 8 † 8 3 ( 8 8 ) 5 * ")
print(" † ; 4 6 ( ; 8 8 * 9 6 * ? ; 8 ) * ‡ ( ; ")
print(" 4 8 5 ) ; 5 * † 2 : * ‡ ( ; 4 9 5 6 * 2 ")
print(" ( 5 * - 4 ) 8 ¶ 8 * ; 4 0 6 9 2 8 5 ) ; ")
print(" ) 6 † 8 ) 4 ‡ ‡ ; 1 ( ‡ 9 ; 4 8 0 8 1 ; ")
print(" 8 : 8 ‡ 1 ; 4 8 † 8 5 ; 4 ) 4 8 5 † 5 2 ")
print(" 8 8 0 6 * 8 1 ( ‡ 9 ; 4 8 ; ( 8 8 ; 4 ( ")
print(" ‡ ? 3 4 ; 4 8 ) 4 ‡ ; 1 6 1 ; : 1 8 8 ; ")
print(" ‡ ? ; ")
print("\n")

mensaje = "53‡‡†305))6*;4826)4‡.)4‡);806*;48†8¶60))85;1‡(;:‡*8†83(88)5*†;46(;88*96*?;8)*‡(;485);5*†2:*‡(;4956*2(5*-4)8¶8*;4069285);)6†8)4‡‡;1(‡9;48081;8:8‡1;48†85;4)485†528806*81(‡9;48;(88;4(‡?34;48)4‡;161;:188;‡?;"

total = len(mensaje)

print(colored('5', 'green') + ' aparece ' + colored(str(mensaje.count("5")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("5")/total , 4)) + '%' , 'red') )
print(colored('3', 'green') + ' aparece ' + colored(str(mensaje.count("3")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("3")/total , 4)) + '%' , 'red') )
print(colored('‡', 'green') + ' aparece ' + colored(str(mensaje.count("‡")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("‡")/total , 4)) + '%' , 'red') )
print(colored('†', 'green') + ' aparece ' + colored(str(mensaje.count("†")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("†")/total , 4)) + '%' , 'red') )
print(colored('0', 'green') + ' aparece ' + colored(str(mensaje.count("0")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("0")/total , 4)) + '%' , 'red') )
print(colored(')', 'green') + ' aparece ' + colored(str(mensaje.count(")")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count(")")/total , 4)) + '%' , 'red') )
print(colored('6', 'green') + ' aparece ' + colored(str(mensaje.count("6")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("6")/total , 4)) + '%' , 'red') )
print(colored('*', 'green') + ' aparece ' + colored(str(mensaje.count("*")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("*")/total , 4)) + '%' , 'red') )
print(colored(';', 'green') + ' aparece ' + colored(str(mensaje.count(";")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count(";")/total , 4)) + '%' , 'red') )
print(colored('4', 'green') + ' aparece ' + colored(str(mensaje.count("4")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("4")/total , 4)) + '%' , 'red') )
print(colored('8', 'green') + ' aparece ' + colored(str(mensaje.count("8")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("8")/total , 4)) + '%' , 'red') )
print(colored('2', 'green') + ' aparece ' + colored(str(mensaje.count("2")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("2")/total , 4)) + '%' , 'red') )
print(colored('.', 'green') + ' aparece ' + colored(str(mensaje.count(".")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count(".")/total , 4)) + '%' , 'red') )
print(colored('¶', 'green') + ' aparece ' + colored(str(mensaje.count("¶")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("¶")/total , 4)) + '%' , 'red') )
print(colored('1', 'green') + ' aparece ' + colored(str(mensaje.count("1")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("1")/total , 4)) + '%' , 'red') )
print(colored('(', 'green') + ' aparece ' + colored(str(mensaje.count("(")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("(")/total , 4)) + '%' , 'red') )
print(colored(':', 'green') + ' aparece ' + colored(str(mensaje.count(":")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count(":")/total , 4)) + '%' , 'red') )
print(colored('9', 'green') + ' aparece ' + colored(str(mensaje.count("9")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("9")/total , 4)) + '%' , 'red') )
print(colored('?', 'green') + ' aparece ' + colored(str(mensaje.count("?")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("?")/total , 4)) + '%' , 'red') )
print(colored('-', 'green') + ' aparece ' + colored(str(mensaje.count("-")), 'yellow' ) + ' veces -' + colored(str(round(mensaje.count("-")/total , 4)) + '%' , 'red') )
print("\n")

diccionario = dict()
diccionario = {
        '5':'A',
        '3':'G',
        '‡':'O',
        '†':'D',
        '0':'L',
        ')':'S',
        '6':'I',
        '*':'N',
        ';':'T',
        '4':'H',
        '8':'E',
        '2':'B',
        '.':'P',
        '¶':'V',
        '1':'F',
        '(':'R',
        ':':'Y',
        '9':'M',
        '?':'U',
        '-':'C',
        ']':'W'
}


print(colored('Mensaje descifrado: \n', 'green'))

descifra = ""
for i in range(len(mensaje)):
    descifra = descifra+""+diccionario[mensaje[i]]

print(descifra)





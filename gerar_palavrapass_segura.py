#este programa vai gerar uma palavra pass segura sorteada 
import random
a_m = "ABCDEFGHIJKLMNOPRSTUVXYZ"
A_mim = a_m.lower()
A_simbolos = "!+.,;:?=_-/"
a_numeros = "0123456789"
ppass = " "
pos = " "

for i in range(8):
    sitio = random.randint(0,4)
    if sitio == 1:
        for i in range(2):
            pos = random.randint(0,len(a_m))
            ppass = ppass + a_m[pos]
    if sitio == 2:
        for i in range(2):
            pos = random.randint(0,len(A_mim))
            ppass = ppass + A_mim[pos]
    if sitio == 3:
        for i in range(2):
            pos = random.randint(0,len(A_simbolos))
            ppass = ppass + A_simbolos[pos]
    if sitio == 4:
        for i in range(2):
            pos = random.randint(0,len(a_numeros))
            ppass = ppass + a_numeros[pos]

print(ppass)
#ira verificar se a palavra pass é segura

a_m = "ABCDEFGHIJKLMNOPRSTUVXYZ"
A_mim = a_m.lower()
A_simbolos = "!+.,;:?=_-/"
a_numeros = "0123456789"
tem_m = False
tem_min = False
tem_s = False
tem_n = False

password = input("intruduza a palavra pass: ")

#testar se tem maiulculas

for letra in a_m:
    if letra in password:
        tem_m = True
        break

#testar se tem minusculas

for letra in A_mim:
    if letra in password:
        tem_min = True
        break

#testar se tem caracteres

for letra in A_simbolos:
    if letra in password:
        tem_s = True
        break

#testar se tem numeros

for letra in a_numeros:
    if letra in password:
        tem_n = True
        break

if tem_m == True and tem_min == True and tem_n == True and tem_s == True and len(password) < 8:
    print("Palavra pass segura.")
else:
    print("Palavra pass não é segura.")

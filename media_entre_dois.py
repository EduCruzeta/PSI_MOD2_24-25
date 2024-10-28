"""
um programa para ler 20 numeros inteiros do utilizador 
e fazer a media dos numeros entre 20 e 50, inclusive [20,50]
"""
soma = 0
contar = 0
for i in range(21):
    numero = int(input("insira o nº"))
    if numero >= 20 and numero <= 50:
        soma = soma + numero
        contar = contar + 1

media = soma / contar

print("A media dos nº entre [20,50] foi de",media)
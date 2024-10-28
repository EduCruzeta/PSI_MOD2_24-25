#este algoritmo vai dizer quantas vogais tem uma frase
contar = 0
frase = input("escreva uma frase:")

for letra in frase:
    if letra in "aeiouAEIOU":
        contar = contar + 1

print("A frase indicada tem",contar,"vogais")
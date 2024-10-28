#Exercicio de passar o fluxo grama para pyton


contar = 0

while contar < 5:
    n = int(input("insira numeros acima de 10 e a baixo de 100: "))

    if n > 10 and n < 100:
        contar = contar + 1

    print (contar)


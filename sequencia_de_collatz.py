"""este algortimo vai calcular os numero de collatez com base se for par 
divide por 2 se for impar multiplica por 3 e adiciona 1
"""
contar = 0
numero = int(input("insira um numero inteiro positivo: "))

while numero != 1:
    if numero % 2 == 0:
        numero = numero // 2
        print(numero)
        contar = contar + 1
    else:
        numero = numero * 3 + 1
        print(numero)
        contar = contar + 1


print("O numero de passos nessesario para chegar a 1 foi de",contar)
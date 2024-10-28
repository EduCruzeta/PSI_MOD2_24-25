#o algoritmo vai pedir dois numeros ao utilizador e vai somar

numero1 = int(input("insira o primeiro nº"))
numero2 = int(input("insira o segundo nº"))

numero2 = numero2 + 1

soma = 0

for i in range(numero1,numero2):
    soma = soma + i

print(soma)
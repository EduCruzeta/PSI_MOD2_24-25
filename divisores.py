#este algoritmo vai ler os numeros do utilizador e vai mostrar todos os divisores dele

numero = int(input("introduza o seu numero: "))

for divisor in range(numero,0,-1):
    if numero % divisor == 0:
        print(divisor)

print("agora com o while")

numero = int(input("introduza o seu numero: "))

divisor = numero

while divisor > 0:
    if numero % divisor == 0:
        print(divisor)
    divisor = divisor - 1
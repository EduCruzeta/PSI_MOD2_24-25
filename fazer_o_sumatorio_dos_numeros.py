#este algoritmo vai somar os numeros que o utilizador indicar

numero1 = int(input("insira o primeiro nº:"))
numero2 = int(input("insira o segundo nº:"))

somatorio = 0

if numero1 < numero2:
    for i in range(numero1,numero2+1):
        somatorio = somatorio + i
else:
    for i in range(numero2,numero1+1):
        somatorio = somatorio + i

print("A soma de todos os numeros é",somatorio)
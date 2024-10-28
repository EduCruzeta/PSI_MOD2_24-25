#este algoritmo vai fazer que o utilizador possa colocar a ordem que quiser

numero1 = int(input("insira o primeiro nº:"))
numero2 = int(input("insira o segundo nº:"))

soma = 0

if numero1 < numero2:
    for i in range(numero1,numero2+1):
        soma = soma + i
else:
    for i in range(numero2,numero1+1):
        soma = soma + i

print(soma)
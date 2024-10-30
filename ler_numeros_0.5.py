#este programa vai mostrar os 10 numeros seguintes a acrecentar por 0.5 no fim mostra a soma de todos os valores~
contar = 0
numero = float(input("insira o seu numero: "))

for i in range (10):
    if i < 9:
        print(numero,end=",")
    else:
        print(numero,end=" ")
    numero = numero + 0.5
    contar = contar + numero

print("=",contar)

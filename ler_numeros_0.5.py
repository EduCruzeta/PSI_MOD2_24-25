#este programa vai mostrar os 10 numeros seguintes a acrecentar por 0.5 no fim mostra a soma de todos os valores~
contar = 0
numero = float(input("insira o seu numero: "))

for i in range (10):
    numero = numero + 0.5
    print(numero,end=",")
    contar = contar + numero

print("=",contar)

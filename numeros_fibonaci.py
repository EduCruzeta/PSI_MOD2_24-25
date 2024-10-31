#este rograma vai mostrar os valorers do fibonaci ate a determinada 

numero = int(input("insira o numero da serie que pretende do fibonaci: "))

x1 = 0
x2 = 1

print(x1,"\n",x2)

for i in range(numero-2):
    soma = x1 + x2
    print(soma)
    x1 = x2
    x2 = soma
    
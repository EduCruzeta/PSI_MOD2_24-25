#este algoritmo vai dizer quais sao os numeros perfeitos ou nao perfeito

nº = int(input("insira o numero: "))
soma = nº
for i in range (1,nº):
    if nº % i == 0:
        soma = soma - i

if soma == 0:
    print("numero perfeito")

else:
    print("o numero nao é perfeito")


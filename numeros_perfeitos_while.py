#este algoritmo vai testar varios numeros perfetos


nº = int(input("intruduza o limite maximo de teste para numero perfeito: "))
for k in range (1,nº):
    soma = 0
    for i in range (1,k):
        resto = k % i
        if resto == 0:
            soma = soma + i

    if soma == k:
        print(f"numero", k ," é perfeito")

    else:
        print(f"o numero",k,"nao é perfeito")
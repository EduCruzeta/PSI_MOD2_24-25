#este algoritmo vai indicar se o numero indicado é primo ou nao

numero = int(input("insira o seu numero:"))

primo = True

for n in range(2,numero):
    if numero % n == 0:
        primo = False
        break
    
if primo == True:
    print(" O nº",numero,"é primo")
else:
    print("O nº",numero,"não é primo")
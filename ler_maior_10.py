# o algoritmo vai ler 10 numeros do utilizador e vai dizer qual é o maior

n = int(input("intruduza o primeiro numero:"))

maior = n
pos_maior = 1
for i in range(9):
    n = int(input("intruduza o primeiro numero:"))
    if n > maior:
        maior = n
        pos_maior = i+1
print("O maior numero é",maior,"e foi o",pos_maior,"º a ser inserido")
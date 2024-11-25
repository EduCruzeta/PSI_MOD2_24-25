"""este algortimo vai ler o numero de passageiros e os bilhetes e o aviao 
so sai quando estiver cheio tambem vai guardar o nome dos passageiros"""
todos_nomes = ""
contar = 0
lugares = int(input("insira o numero de lugares do avião: "))
bilhetes = int(input("insira o numero de bilhetes que foram vendidos: "))

if bilhetes > lugares:
    print("O numero de bilhetes vendidos nao pode ser maior que o numero de lugares insira novamente: ")
    bilhetes = int(input("insira o numero de bilhetes que foram vendidos: "))

while bilhetes > 0:
    nome = input("insira o nome do passageiro: ")
    todos_nomes = todos_nomes + nome + "\n"
    bilhetes = bilhetes - 1
    contar = contar + 1
    if nome == "":
        print("O programa ira terminar.")
        break
    
print(todos_nomes "tem cerca de",contar - 1)



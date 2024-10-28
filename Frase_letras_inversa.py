#este programa vai ler uma frase do utilizador e vai escrever letra por letra por ordem inversa

frase= input("Insira uma frase:")

for i in range(len(frase) -1,-1,-1):
    print(frase[i])
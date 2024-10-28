#ler uma palavra e ver se é igual de traz para frente 

nome = input("intruduza uma palavra:")

pinvertida =""

for i in range(len(nome)-1,-1,-1):
    pinvertida = pinvertida + nome[i] 

if nome == pinvertida:
    print("É um palindromo")
else:
    print("Não é um palindromo")
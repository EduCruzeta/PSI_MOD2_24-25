#algoritmo que le dois nomes e diz qual o maior

nome1 = input("digite o primeiro nome:")
nome2 = input("digite o segundo nome:")

if len(nome1) > len(nome2):
    print("o maior nome é",nome1,"com",len(nome1),"letras")
elif len(nome1) == len(nome2):
    print("Os nomes",nome1,"e",nome2,"tem a mesma quantidade de letras ambos com",len(nome2))
else:
    print("o maior nome é",nome2,"com",len(nome2))

#este algoritmo vai ler dois nomes e dizer qual o maior

nome1 = input("digite o primeiro nome:")
nome2 = input("digite o segundo nome:")

letras1 = len(nome1)
letras2 = len(nome2)

if letras1 > letras2:
    print("o maior nome é",nome1,"com",letras1,"letras")
elif letras1 == letras2:
    print("Os nomes",nome1,"e",nome2,"tem a mesma quantidade de letras ambos com",letras2)
else:
    print("o maior nome é",nome2,"com",letras2,)
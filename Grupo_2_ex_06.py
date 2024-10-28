#algoritmo numeros iguais ou maior 
n1 = int(input("introduza um valor inteiro:"))
n2 = int(input("introduza um valor inteiro:"))

if n1 == n2:
    print("Os numeros são iguais")
else:
    if n1 > n2:
        print("O maior numero é",n1)
    else:
        print("O maior numero é",n2)
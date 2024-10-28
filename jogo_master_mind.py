#jogo de advinhar um valor
import random
numero_secreto = random.randint(1,10)
print(numero_secreto)
x = int(input("insira um numero:"))

if x == numero_secreto:
    print("parabens acertou o numero")
else:
    if x > numero_secreto:
        print("O numero é menor")
    else:
        print("O numero é maior")
        x = int(input("insira um numero:"))
        if x == numero_secreto:
            print("parabens acertou o numero")
        else:
            if x > numero_secreto:
                print("O numero é menor")
            else:
                print("O numero é maior")
                x = int(input("insira um numero:"))
                if x == numero_secreto:
                    print("parabens acertou o numero")
                else:
                    if x > numero_secreto:
                        print("O numero é menor")
                    else:
                        print("O numero é maior")
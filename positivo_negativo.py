#este algoritmo vai indicar se o numero é positivo iu negativo e quando intruduzir o zero vai parar

n = 1
while n != 0:
    n = int(input("intruduza o seu numero:"))
    if n > 0:
        print("O numero",n,"é positivo")
    elif n < 0:
        print("O numero",n,"é negativo")
    else:
        print("O numero é zero, acabar programa!")

# o algoritmo vai pedir ao utilizador a operacao que ele quer e vai fazer apenas essa
pergunta = "sim"
resultado = 0
while pergunta == "sim":
    operacao = input("diga qual operação vai fazer soma,subtração,divisão,somatorio ou multiplicação: ")

    numero1 = int(input("insira o primeiro numero:"))
    numero2 = int(input("insira o segundo numero:"))

    if operacao == "soma":
        resultado = numero1 + numero2

    elif operacao == "subtração":
        resultado = numero1 - numero2

    elif operacao == "divisão":
        resultado = numero1 / numero2
    
    elif operacao == "multiplicação":
        resultado = numero1 * numero2
    
    elif operacao == "somatorio":
        if numero1 < numero2:
            for i in range(numero1,numero2+1):
                resultado = resultado + i
        else:
            for i in range(numero2 + 1,numero1,-1):
                resultado = resultado + i
    
    print(resultado)
    pergunta = input("deseja continuar a fazer contas? " )
    pergunta = pergunta.lower()

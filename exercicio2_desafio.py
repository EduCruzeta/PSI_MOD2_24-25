#este algoritmo vai fazer a operacao de elevacao de um numero se o opererador aritmetrico ^
resultado = 0
valor1 = int(input("insira o primeiro valor: "))
valor2 = int(input("insira o segundo valor: "))

for i in range(1,valor2+1):
    resultado = resultado * valor1

print("O valor da conta",valor1,"elevado a,",valor2,"é,",resultado)
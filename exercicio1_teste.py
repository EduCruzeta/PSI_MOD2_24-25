#este algoritmo vai fazer de multibanco

saldo_i = float(input("Saldo inicial: "))
n_conta = int(input("Nº da conta: "))
operacao = input("Qual a operação (L)levantar (D)deposito: ")
valor = float(input("Valor da operação: "))
saldo_f = saldo_i
if valor <= 0:
    print("Valor da operação não é valida")
else:
    if operacao.lower() == "l":
        saldo_f = saldo_i - valor
    elif operacao.lower() == "d":
        saldo_f = saldo_i + valor
    else:
        print("Operação inválida")
    print("Nº da conta",n_conta) 
    if saldo_f < 0:
        print("O seu saldo não permite a operação") 
    else:
        print("Saldo inicial:",round(saldo_i,2))
        print("Saldo final:",round(saldo_f,2))
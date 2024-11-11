#este programa vai fazer de caixa atm
import math
dinheiro = 0
atm = "funcionar"

while atm == "funcionar":
    print("""ATM 
1. Ver Saldo
2. Depositar Dinheiro
3. Levantar Dinheiro
4. Terminar """)
    escolha = int(input(":"))
    if escolha == 1:
        print(dinheiro)
    elif escolha == 2:
        deposito = float(input("Insira a quantidade que deseja depositar: "))
        #testar o numero de casas decimais
        d = deposito - round(deposito,2)
        if d !=0:
            print("O valor não é valido.")
        if deposito >= 0.01 and deposito <= 10000:
            dinheiro = dinheiro + deposito
        else:
            print("O valor do deposito esta incorreto.")
    elif escolha == 3:
        levantar = float(input("Insira a quantidade que deseja levantar: "))
        d = levantar - round(deposito,2)
        if d !=0:
            print("O valor não é valido.")
        if levantar >= 10 and levantar <= 400:
            dinheiro = dinheiro - levantar
        else:
            print("O valor de levantamento esta a cima do permitido.")
        
        while dinheiro < 0:
            print("2. Depositar Dinheiro")
            escolha = int(input(":"))
            if escolha == 2:
                deposito = float(input("Insira a quantidade que deseja depositar: "))
                if deposito >= 0.01 and deposito <= 10000:
                    dinheiro = dinheiro + deposito

    elif escolha == 4:
        print("O programa ira terminar.")
        atm = "terminar"
    else:
        print("A escolha nao foi valida tente novamente")
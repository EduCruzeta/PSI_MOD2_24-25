#este programa vai ajudar o utilizador a saber oque acontece ou quantos pontos sobram na sua carta 
carta = 12
temp = 0
perdacartamg = 0
perdacartag = 0
print("Tem 12 pontos na sua carta de condução")

print("""Escolha uma opção:
1. Infração muito grave
2. Infração grave
3. Infração leve
4. Terminar """)

while carta != 0:  
    escolha = int(input("insira a sua escolha: "))
    if escolha == 1:
        carta = carta - 6
        perdacartamg = perdacartamg + 1
    elif escolha == 2:
        carta = carta - 4
        perdacartag = perdacartag + 1
    elif escolha == 3:
        if temp == 0:
            temp = temp + 1
            print("Se voltar a cometer uma Infração leve ira perder 1 ponto da sua carta.")
        else:
            carta = carta - 1
    elif escolha == 4:
        print("O programa vai ser encerrado.")
        break
    if perdacartamg == 1 and perdacartag == 1:
        print("Cometeu una infração muito grave e uma infração grave ira ficar sem a carta por 1 ano.")
        continue
    if perdacartag == 2 or perdacartamg == 2:
        print("Cometeu 2 infrações graves ira ficar sem a carta por 1 ano")
        continue
    if carta > 0:
        print("Tem",carta,"pontos na sua carta")
    else:
        print("Os pontos da sua carta acabaram.")
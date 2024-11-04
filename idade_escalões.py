# este algoritmo vai com base na idade indicar qual a classe do jogador

idade = int(input("insira a idade do jogador: "))

if idade < 10:
    print("O jogador pertence a clase infantis.")
elif idade >= 10 and idade < 14:
    print("O jogador pertence a classe iniciados.")
elif idade >= 14 and idade < 18:
    print("O jogador pertence a classe juniores.")
elif idade >= 18:
    print("O jogador pertence a classe senior.")
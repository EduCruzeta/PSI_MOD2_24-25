#este algoritmo vai dizer todos os anos bixetos

ano = int(input("insira o ano que deseja ver se é bissexto: "))

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print('Ano bissexto.')
else:
    print('Não é um ano bissexto.')
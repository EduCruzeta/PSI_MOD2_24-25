#este algoritmo vai calcular a media de 10 alunos
soma = 0
for i in range(1,11):
    notas = int(input("insira a nota dos alunos:"))
    soma = notas + soma

media = soma / 10

print("o valor da media é",media)


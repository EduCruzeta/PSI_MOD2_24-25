#este algoritmo vai calcular a media de 10 alunos e dizer o numero de positivos e negativos
Constante_alunos = 10
soma = 0
notas_positivas = 0
notas_negativas = 0
for i in range(Constante_alunos):
    notas = int(input("insira a nota dos alunos:"))
    soma = notas + soma
    if notas >= Constante_alunos:
        notas_positivas = notas_positivas + 1
    else:
        notas_negativas = notas_negativas + 1

media = soma / Constante_alunos
perpositivas = notas_positivas / Constante_alunos * 100 
pernegativas = notas_negativas / Constante_alunos * 100 
print("o valor da media é",media,"e houve",notas_positivas,"positivas ou",perpositivas,"% e",notas_negativas,"negativas ou",pernegativas,"%")
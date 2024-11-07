# o programa vai ler as notas de uma tuma e indicar que qual foi a maior nota da turma

melhor_nota = -1
numero_aluno = -1

nr_alunos = int(input("quando alunos tem a tuma: "))

for i in range(nr_alunos):
    nota = int(input("insira a nota do aluno: "))
    if nota > melhor_nota:
        melhor_nota = nota
        numero_aluno = i + 1

print("O aluno com a melhor nota é o aluno Nº,",numero_aluno,"com uma nota de",melhor_nota,"valores")
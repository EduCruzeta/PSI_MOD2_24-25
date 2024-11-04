# O algoritmo vai ler as 5 voltas do utilizador e vai no fim dizer a duracao total das 5 voltas

tempo = 0
pergunta = "sim"

tempovoltas = int(input("insira a duração da volta em segundos: "))
tempo = tempo + tempovoltas

if tempovoltas <= 0:
    print("O valor da volta não é aceitavel.")

for i in range(2,6):
    tempovoltas = int(input("insira a duração da volta em segundos: "))
    tempo = tempo + tempovoltas

tempomin = tempo //  60
segundos = tempo % 60

print("A duração total das voltas é de",tempomin,"minuto e",segundos,"segundos")
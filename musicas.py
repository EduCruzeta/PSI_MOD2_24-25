"""
um programa para calcular a duracao tootal de um album. 
Para isso é nessesário insirir a duração de cada musica.
A duração da musica. A duração não pode ser inferior ou igual a 0 nem pode ser superior a 100 minutos

"""
tempo = 0
pergunta = "sim"

pedir_musica = int(input("insira a duração da musica em segundos: "))
tempo = tempo + pedir_musica

if pedir_musica <= 0:
            print("O valor da musica não é aceitavel.")

while pergunta == "sim":
    pergunta = (input("deseja inserir mais musicas? "))
    if pergunta == "sim":
        pedir_musica = int(input("insira a duração da sua musica me segundos: "))
        if pedir_musica <= 0:
            print("O valor da musica não é aceitavel.")
        else:
            tempo = tempo + pedir_musica

tempomin = tempo //  60
segundos = tempo % 60

print("A duração total das musicas é de",tempomin,"minuto e",segundos,"segundos")
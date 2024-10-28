#Este programa vai ler 10 letras do utilizador e vai dizer quantas vogais introduziu
contar = 0
for i in range(10):
    letra = input("insira a sua letra: ")
    letra = letra.lower()
    if letra in "aeiou":
        contar = contar + 1
    
print("inseriu",contar,"vogais")
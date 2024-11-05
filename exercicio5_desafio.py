#este algoritmo vai ler os votos inseridos e no fim quando carregar em "0" ira terminar e mostrar os resultados

votos = "decorrer"
contart = 0
contars = 0
contarh = 0
contarf = 0
voto = ""

while votos == "decorrer":
    print(""" Listas Candidatas:
          1- Lista T
          2- Lista S
          3- Lista H
          4- Lista F""")
    voto = input("insira a letra da lista que quer votar: ")
    voto = voto.upper()
    if voto == "T" :
        contart = contart + 1
    elif voto == "S" :
        contars = contars + 1
    elif voto == "H" :
        contarh = contarh + 1
    elif voto == "F" :
        contarf = contarf + 1
    elif voto == "0":
        print("O resultado final das listas são lista T com",contart,"votos, lista S com",contars,"votos, lista H com",contarh,"e por fim lista F com",contarf,"votos")
        print("O programa ira terminar parabens a lista vencedora.")
        votos = "acabou"
    else:
        print("A lista inserida é inválida")

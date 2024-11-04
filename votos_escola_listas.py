#este algoritmo vai ler os votos inseridos e no fim quando carregar em "0" ira terminar e mostrar os resultados

votos = "decorrer"
contart = 0
contars = 0
voto = ""

while votos == "decorrer":
    print(""" Listas Candidatas:
          1- Lista T
          2- Lista S""")
    voto = input("insira a letra da lista que quer votar: ")
    voto = voto.upper()
    if voto == "T" :
        contart = contart + 1
    elif voto == "S" :
        contars = contars + 1
    elif voto == "0":
        print("O resultado final das listas são lista T com",contart,"votos e lista S com",contars,"votos")
        print("O programa ira terminar parabens a lista vencedora.")
        votos = "acabou"
    else:
        print("A lista inserida é inválida")

#este algoritmo vai ler o peso de todas as malas ate exeder os 1000kg 
peso = "aguenta"
aviao = 1000
while peso == "aguenta":
    pesomalas = float(input("insira o peso da mala: "))
    aviao = pesomalas - aviao
    if aviao > 0:
        print("exedeu o limite de peso o avião não pode levar mais.")
        peso = "nao aguenta"
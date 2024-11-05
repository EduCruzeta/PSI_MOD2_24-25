#este algoritmo vai ler o peso de todas as malas ate exeder os 1000kg 
aviao = 1000
pesomalas = 0
contar = 0
taxa = 0
while aviao > contar:
    pesomalas = float(input("insira o peso da mala: "))
    taxa = taxa + 1
    contar = contar + pesomalas

print("exedeu o limite de peso o avião não pode levar mais.")
taxa = taxa * 20
print("O total das taxass a pagar pela carga é de",taxa,"euros")
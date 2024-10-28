#algoritimo ler 3 notas e media é positiva 
N1 = int(input("insira a 1 nota:"))
N2 = int(input("insira a 2 nota:"))
N3 = int(input("insira a 3 nota:"))

Media = (N1 + N2 + N3) / 3

if Media >= 10:
    print("positiva")
else:
    print("negativa")
#algoritmo maior numero
x1 = int(input("insira um numero:"))
x2 = int(input("insira um numero:"))
x3 = int(input("insira um numero:"))

if x1 > x2:
    if x1 > x3:
        print(f"o maior é o {x1}")
        
# verificar o x2

if x2 > x1:
    if x2 > x3:
        print(f"o maior é o {x2}")

#verificar o x3

if x3 > x2:
    if x3 > x2:
        print(f"o maior é o {x3}")
        

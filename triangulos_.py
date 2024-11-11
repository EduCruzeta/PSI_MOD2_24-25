#este algortimo vai ler os lados do triangulo e dizer que tipo de triangulo é.

a=int(input("insira o valor do lado A: "))
b=int(input("insira o valor do lado B: "))
c=int(input("insira o valor do lado C: "))

if a >= 1 and b >= 1 and c >= 1:
    if (a+b)>c and (b+c)>a and (a+c)>b:
        if a == b and a == c and b == c:
            print("triangulo Equilátero tem todos os lados iguais")
        elif a != b and b != c and c != a:
            print("triagulo Escaleno tem todos os lados diferentes")
        else:
          print("triangulo Isósceles tem dois lados iguais")
    else:    
        print("Os valores dos triangulos estao incorretos nãos pode ser um triangulo.")    
else:
    print("o triangulo nao pode ser testado porque tem valores negativos.")

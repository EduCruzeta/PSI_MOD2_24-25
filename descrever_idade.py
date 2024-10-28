#descrever idade
idade = int(input("insira a sua idade:"))

if idade < 0 or idade > 120:
    print("A sua idade é invalida")
else:
    if idade >= 0 and idade <= 11:
        print("esta na infancia") 
    else:
        if idade >= 12 and idade <= 20:
            print("esta na adolescência")
        else:
            if idade >= 21 and idade <= 75:
                print("esta na idade adulta")
            else:
                if idade >= 75 and idade <= 120:
                    print("esta na velhice")
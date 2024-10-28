#mostrar todos os numeros positivos sem os que sao divisiveis por 3

for i in range(1,100):
    if i % 3 != 0:
        print(i)
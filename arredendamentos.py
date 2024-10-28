#arredondamentos 
import math #importar a biblioteca de funções 

x = 11.1

print(math.ceil(x))# arredonda sempre para o inteiro seguinte
print(math.floor(x)) # arredonda sempre para o inteiro a baixo ou anterior

print(int(x)) #converter para o initeiro sem arredondar
print(round(x,1)) # arredonda para o numero par mais proximo

#arredondar para cima se a parte decimal >= 0.5
parte_decimal = x - int(x)
if parte_decimal >= 0.5:
    x = int(x) + 1
else:
    x = int(x)

print(x)
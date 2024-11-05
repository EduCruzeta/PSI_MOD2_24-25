"""
Construa o algoritmo do fatorial de um número, isto é, o produto de todos os inteiros desde 
1 até ao número escolhido. Por exemplo, o fatorial de 3 é 1 x 2 x 3 = 6, mas o fatorial de zero 
é 1.
"""

n = int(input("insira um numero: "))

for i in range (1,n+1):
    print(i*i)
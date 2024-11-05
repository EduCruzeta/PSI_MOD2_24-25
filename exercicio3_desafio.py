"""
este algortimo vai pedir a temperatura da sala entra as 9 e as 17
 a cada hora e dizer qual foi a minima e a maxima ao longo do dia
"""

tempmaxima = 0
tempminima = 1000

for i in range (9,18):
    temp = int(input("indique a temperatura da sala: "))
    if temp > tempmaxima:
        tempmaxima = temp 

    if temp < tempminima:
        tempminima = temp

print("A temperatura maxima atingida foi",tempmaxima,"graus e a temperatura minima foi de",tempminima,"graus")
#algoritmo fatias de pizza
f1 = int(input("insira o numero de fatias que o 1 amigo comeu:"))
f2 = int(input("insira o numero de fatias que o 2 amigo comeu:"))
f3 = int(input("insira o numero de fatias que o 3 amigo comeu:"))
P = int(input("insira o preço da pizza:"))
TF = f1 + f2 + f3 
P1 = f1 / TF 
P2 = f2 / TF
P3 = f3 / TF
Vp1 = P1 * P
Vp2 = P2 * P
Vp3 = P3 * P
print("O amigo 1 vai pagar",Vp1,"€ o amigo 2 vai pagar",Vp2,"€ o amigo 3 vai pagar",Vp3,"€")
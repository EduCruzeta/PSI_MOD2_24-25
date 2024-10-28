#resolução do exercício 01 do grupo II
p1 = int(input("Intruduza os minutos de passagem no ponto 1:"))
p2 = int(input("intruduza os minutos de passagem no ponto 2:"))
distancia = int(input("intruduza a distancia (metros)"))

duracao_m = p2 - p1

duracao_S = duracao_m * 60

v_media = distancia / duracao_S

print(f"{v_media:.3f} m/s")
# O algoritmo vai ler o numero de mesas e pessoas e indicar se ja esta cheio ou nao

mesas = 10
lugares = mesas * 5

while mesas>0:
    n_clientes = int(input("quantas pessoas para entrar:"))
    if n_clientes>lugares:
        print("Não tem lugares para tantos clientes")
        break
    mesas = mesas - 1
    lugares = lugares - n_clientes
    print("Mesas disponiveis:",mesas)
    print("Lugares disponíveis: ",lugares)

print("As mesas ja foram todas ocupadas.")
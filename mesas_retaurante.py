#este algoritmo vai ler as mesas e os lugares e indicar a disponibilidade

mesas = 10
lugares = mesas * 5

for mesas_ocupadas in range(mesas):
    n_clientes = int(input("quantas pessoas para entrar:0"))
    if n_clientes>lugares:
        print("Não tem lugares para tantos clientes")
        break
    mesas = mesas - 1
    lugares = lugares - n_clientes
    print("Mesas ocupadas: ",mesas_ocupadas)
    print("Lugares disponíveis: ",lugares)
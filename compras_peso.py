# o algortimo vai dizer o preço a quantidade de produtos e o peso

orcamento = float(input("insira o seu orçamento:"))
peso_possivel = float(input("insira a quantidade de peso que consegue carregar:"))

while orcamento > 0 and peso_possivel > 0:
    preco = float(input("insira o preço do seu artigo:"))
    if preco == 0:
        break
    peso = float(input("insira o peso do artigo:"))
    if orcamento < preco or peso < peso_possivel:
        print("Não tem dinheiro para esse artigo ou o artigo é muito pesado:")
    else:
        orcamento = orcamento - preco
        peso = peso - peso_possivel
    print("Ainda tem",orcamento,"€ e ainda pode carregar mais",peso,"kg de produto")
print("acabou as suas compras.")
    
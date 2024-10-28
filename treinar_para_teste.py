#teste para ajudar no teste com percentagens
x = int(input("insira a quantidade de produtos"))

desconto = 0
if x >= 500 or 1000:
    desconto = 5/100
elif x > 1000:
    desconto = 8/100

preco = 1000 * x

valor_desconto = preco * desconto

preco_final = preco - valor_desconto

print ("o valor é de",preco_final)
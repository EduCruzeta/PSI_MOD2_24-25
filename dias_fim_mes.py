#este algoritmo vai dizer quantos dias faltam para o fim do mes
soma = 0
dias_falta = 0
dia = int(input("insira o dia do mes: "))
mes = int(input("insira o mes: "))
ano = int(input("insira o ano: "))

if mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        dias_falta = 29 - dia
        print("faltam",dias_falta,"dias para o fim do mes")
    else:
        dias_falta = 28 - dia
        print("faltam",dias_falta,"dias para o fim do mes")
    
if mes in (1,3,5,7,8,10,12):
    dias_falta = 31 - dia
    print ("faltam",dias_falta,"dias para o fim do mes")
elif mes in (4,6,9,11):
    dias_falta = 30 - dia
    print("faltam",dias_falta,"dias para o fim do mes")
    
for i in range (mes,13):
    if i in (1,3,5,7,8,10,12):
        soma = soma + 31
    elif i in (4,6,9,11):
        soma = soma + 30
    elif i == 2:
        if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
            soma = soma + 29
        else:
            soma = soma + 28

fimano = soma - dia

print("faltam",fimano,"dias para o fim do ano")
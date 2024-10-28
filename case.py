#algotmo para testar os caso
dia = int(input("insira um número interiro de 1 a 7"))
match dia:
    case 1:
        print("segunda-feira")
    case 2:
        print("terça-feira")
    case 3:
        print("quarta-feira")
    case 4:
        print("quinta-feira")
    case 5:
        print("sexta-feira")
    case 6:
        print("sábado")
    case 7:
        print("domingo")
    case _:
        print("o valor indicado não é")

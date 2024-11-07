# este programa le o email e pass word e depois verifica se esta correto

email = input("insira o seu email:")
password = input ("insira a sua palavra passe:")

print("Login executado com sucesso")

for i in range (3):

    loginemail = input("insira o seu email:")

    loginpassword = input("insira a sua palavra passe:")

    if loginemail == email and password == loginpassword:
        print("Acesso autorizado")
        break 

    elif loginemail != email and loginpassword != password:
        print("Login falhou")

    elif loginemail != email and loginpassword == password:
        print("Email invalido")

    elif loginemail == email and loginpassword != password:
        print("password inválida")

if loginemail != email and loginpassword != password:
    print("Execeu o limite de tentativas.")



#algoritmo verificação de credenciais
email = input("insira o seu email:")
password = input ("insira a sua palavra passe:")

print("Login executado com sucesso")

loginemail = input("insira o seu email:")
loginpassword = input("insira a sua palavra passe:")

if loginemail == email and password == loginpassword:
    print("Acesso autorizado")
else:
    print("O login falhou")
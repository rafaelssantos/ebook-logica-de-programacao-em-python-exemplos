usuario = input("Informe seu e-mail: ")
if usuario == "turing@email.com":
    senha = input("Informe sua senha: ")
    if senha == "12345":
        print("Acesso liberado!")
    else:
        print("Senha incorreta!")
else:
    print("Usuário não encontrado.")
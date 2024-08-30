usuario = input("Digite seu nome de usuário: ")
senha = input("Digite sua senha: ")

if usuario == "turing":
    if senha == "12345":
        print("Bem-vindo, turing!")
    else:
        print("Senha incorreta.")
else:
    print("Nome de usuário não encontrado.")
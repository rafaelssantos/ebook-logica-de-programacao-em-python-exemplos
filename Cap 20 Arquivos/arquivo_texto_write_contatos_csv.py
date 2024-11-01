n = int(input("Quantos contatos deseja gravar? "))
caminho = input("Caminho do arquivo CSV: ")

with open(caminho, "w") as arquivo:
    for e in range(n):
        contato = {}
        contato["Nome"] = input("Nome do contato: ")
        contato["Telefone"] = input("Telefone do contato: ")

        arquivo.write(contato["Nome"] + "," + contato["Telefone"] + "\n")
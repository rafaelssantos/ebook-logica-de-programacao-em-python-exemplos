caminho = input("Informe o caminho para o arquivo de e-mails: ")

with open(caminho) as arquivo:
    for linha in arquivo:
        print("E-mail enviado para " + linha.strip())
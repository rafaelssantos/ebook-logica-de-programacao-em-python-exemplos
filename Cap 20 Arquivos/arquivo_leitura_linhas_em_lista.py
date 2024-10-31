with open("nomes.txt", "r") as arq:
    linhas = arq.readlines()  # Lê todas as linhas do arquivo
    for linha in linhas:       # Itera por cada linha
        print(linha)           # Exibe a linha atual
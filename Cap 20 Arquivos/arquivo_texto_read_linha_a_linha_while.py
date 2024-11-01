with open("nomes.txt", "r") as arq:
   linha = arq.readline()     # Lê a primeira linha
   while linha:               # Enquanto houver linha
      print(linha.strip())            # Exibe a linha atual
      linha = arq.readline()  # Lê a próxima linha
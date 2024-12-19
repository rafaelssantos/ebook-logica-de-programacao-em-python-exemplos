with open("nomes.txt", "r") as arq:
   for linha in arq:        # Itera sobre cada linha do arquivo
      print(linha.strip())
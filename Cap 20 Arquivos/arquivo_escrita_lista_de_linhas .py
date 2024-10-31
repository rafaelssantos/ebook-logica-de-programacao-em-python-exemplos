linhas = ["Açúcar 2 kg\n", "Arroz 5 kg\n", "Feijão 2 kg\n"]  # Lista de produtos
with open("compras.txt", "w") as arq:
    arq.writelines(linhas)  # Escreve todas as linhas no arquivo
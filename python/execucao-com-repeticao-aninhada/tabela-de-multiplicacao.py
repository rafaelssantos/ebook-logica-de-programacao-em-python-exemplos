for i in range(1, 11): # Laço externo: controla as linhas (fatores de 1 a 10)
    for j in range(1, 11): # Laço interno: controla as colunas (fatores de 1 a 10)
        print(f"{i * j:3}", end=" ")  # Imprime o resultado da multiplicação, formatado para 3 espaços
    print() # Quebra de linha após cada linha da tabela
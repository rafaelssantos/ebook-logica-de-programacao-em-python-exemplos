nomes = [] # Inicializa a lista de nomes

# Solicita ao usuário para digitar cinco nomes completos
for i in range(5):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)

# Solicita ao usuário para buscar uma correspondência parcial
nome_busca = input("Digite uma parte do nome que deseja buscar: ")

# Inicializa a lista de correspondências
correspondencias = []

# Verifica se há correspondências parciais na lista
for nome in nomes:
    if nome_busca.lower() in nome.lower():
        correspondencias.append(nome)

# Exibe os resultados
if correspondencias:
    print("Nomes encontrados:")
    for correspondencia in correspondencias:
        print(correspondencia)
else:
    print(f"Nenhum nome encontrado com a parte '{nome_busca}'.")
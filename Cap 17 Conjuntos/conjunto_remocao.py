conjunto = {1, 2, 3}
conjunto.remove(2)  # Remove o elemento 2

# O código abaixo gera um erro já que 4 não está no conjunto
# Comente a linha para executar todo o programa
conjunto.remove(4)

conjunto.discard(3)  # Remove o elemento 3, não gera erro se não estiver presente

print(conjunto)  # 1
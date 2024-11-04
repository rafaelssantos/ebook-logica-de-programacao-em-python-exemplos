produtos_papelaria= {
    "Borracha": 3.50,
    "Caderno": 15.99,
    "Caneta": 2.25,
    "Lápis": 2.50
}

for chave in produtos_papelaria: # Iterando sobre as chaves
    print(chave)
    # Borracha
    # Caderno
    # Caneta
    # Lápis

for valor in produtos_papelaria.values(): # Iterando sobre os valores
    print(valor)
    # 3.5
    # 15.99
    # 2.25
    # 2.5

for chave, valor in produtos_papelaria.items(): # Iterando sobre pares de chave-valor
    print(f"{chave}: {valor}")
    # Borracha: 3.5
    # Caderno: 15.99
    # Caneta: 2.25
    # Lápis: 2.5
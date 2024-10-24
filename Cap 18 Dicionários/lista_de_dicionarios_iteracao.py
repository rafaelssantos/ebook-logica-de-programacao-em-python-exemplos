produtos = [
    {"nome": "Borracha", "preco": 3.50},
    {"nome": "Caderno", "preco": 15.99},
    {"nome": "Caneta", "preco": 2.25},
]

for produto in produtos:
    print(f"Produto: {produto['nome']}, Preço: {produto['preco']}")
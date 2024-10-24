produtos_papelaria= {
    "Borracha": 3.50,
    "Caderno": 15.99,
    "Caneta": 2.25,
    "Lápis": 2.50,
}

print(produtos_papelaria["Borracha"])       # 3.50
print(produtos_papelaria.get("Caneta"))     # 2.25
print(produtos_papelaria["Régua"])          # Erro
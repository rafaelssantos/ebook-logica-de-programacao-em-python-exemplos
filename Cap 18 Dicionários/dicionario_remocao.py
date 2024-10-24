produtos_papelaria= {
    "Borracha": 3.50,
    "Caderno": 15.99,
    "Caneta": 2.25,
    "Lápis": 2.50,
}

produtos_papelaria.pop("Borracha")
del produtos_papelaria["Caderno"]

print(produtos_papelaria) # {'Caneta': 2.25, 'Lápis': 2.5}
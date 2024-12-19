produtos_papelaria= {
    "Borracha": 3.50,
    "Caderno": 15.99,
    "Caneta": 2.25,
    "Lápis": 2.50
}

produtos_copia = produtos_papelaria.copy()
produtos_papelaria["Caneta"] = 2.00

print(produtos_papelaria) 
# {'Borracha': 3.5, 'Caderno': 15.99, 'Caneta': 2.0, 'Lápis': 2.5}
print(produtos_copia) 
# {'Borracha': 3.5, 'Caderno': 15.99, 'Caneta': 2.25, 'Lápis': 2.5}
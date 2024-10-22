conjunto1 = {1, 2, 3}
conjunto2 = {2, 3, 4}

diferenca_simetrica = conjunto1.symmetric_difference(conjunto2)
# ou
diferenca_simetrica = conjunto1 ^ conjunto2

print(diferenca_simetrica)  # Saída: {1, 4}
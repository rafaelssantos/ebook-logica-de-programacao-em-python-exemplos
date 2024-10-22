# Entrada dos valores
valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

# Troca de valores utilizando tupla
valor1, valor2 = valor2, valor1

# Exibe os valores após a troca
print(f"Após a troca, o primeiro valor é {valor1} e o segundo valor é {valor2}.")
import random       # Importação do módulo random

a = int(input("Informe o limite inferior do intervalo: "))
b = int(input("Informe o limite superior do intervalo: "))
num = random.randint(a, b)
print("Número aleatório gerado:", num)
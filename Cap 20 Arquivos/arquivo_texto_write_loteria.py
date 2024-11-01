import random

n = int(input("Quantos números deseja sortear? "))
caminho = input("Informe o caminho do arquivo: ")

numeros_sorteados = set()

while len(numeros_sorteados) < n:
    num = random.randint(1, 100)
    numeros_sorteados.add(num)

with open(caminho, "w") as arquivo:
    for num in numeros_sorteados:
        arquivo.write(str(num) + "\n")
import random

numeros = []

for e in range(100):
    numeros.append(random.randint(0, 1000))

indice = int(input("Você deseja obter o valor de qual posição? "))

print(numeros[indice])
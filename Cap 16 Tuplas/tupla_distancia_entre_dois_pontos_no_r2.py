import math

def distancia(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Exemplo de uso
ponto1 = (float(input("x1: ")), float(input("y1: ")))
ponto2 = (float(input("x2: ")), float(input("y2: ")))

dist = distancia(ponto1, ponto2)
print("A distância entre os pontos é ", dist)
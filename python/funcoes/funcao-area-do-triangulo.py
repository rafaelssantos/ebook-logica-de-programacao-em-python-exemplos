def calcular_area(base, altura):
    area = (base * altura) / 2
    return area

b = float(input("Informe a base: "))
h = float(input("Informe a altura: "))
a = calcular_area(b, h)
print("O valor da área do triângulo é", a)
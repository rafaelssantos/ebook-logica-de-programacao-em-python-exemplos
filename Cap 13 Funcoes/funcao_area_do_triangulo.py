def calc_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

# ---------------------------------------------------------

b = float(input("Informe a base: "))
h = float(input("Informe a altura: "))
a = calc_area_triangulo(b, h)
print("O valor da área do triângulo é", a)
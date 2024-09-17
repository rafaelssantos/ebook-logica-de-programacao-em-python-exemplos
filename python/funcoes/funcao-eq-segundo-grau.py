def calcular_delta(a, b, c):
    delta = b**2 - 4 * a * c 
    return delta

def eq_segundo_grau(a, b, c):
    x1 = (-b + calcular_delta(a, b, c) ** (1/2)) / (2 * a)
    x2 = (-b - calcular_delta(a, b, c) ** (1/2)) / (2 * a)
    return x1, x2

print("Programa que calcula a Equação do Segundo Grau.")
print("ax²+ bx + c = 0")
a = float(input("Informe o valor do coeficiente a: "))
b = float(input("Informe o valor do coeficiente b: "))
c = float(input("Informe o valor do coeficiente c: "))
x1, x2 = eq_segundo_grau(a, b, c)
print("Equação: {a}x² + {b}x + c = 0"}
print("As raízes são {x1} e {x2}.")
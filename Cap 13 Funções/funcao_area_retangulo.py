def calc_area_retangulo(base, altura):
    """
        Função que calcula a área do retângulo.
        Args:
        - base : Base do retângulo
        - altura : Altura do retângulo
        Returns:
            Área calculada
    """
    area = base * altura
    return area

# ----------------------------------------------------
b = float(input("Informe a base: "))
h = float(input("Informe a altura: "))
area = calc_area_retangulo(b, h)
print(area)
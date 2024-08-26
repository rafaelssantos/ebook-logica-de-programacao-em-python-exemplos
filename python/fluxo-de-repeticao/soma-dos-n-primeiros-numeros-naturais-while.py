n = int(input("Informe a quantidade de números da sequência: "))
soma = 0        # O valor 0 é elemento neutro da soma
i = 0
while i < n:
    soma = soma + i   # soma += i
    i = i + 1   # i += i
print("A soma dos", n, "primeiros números naturais é", soma)
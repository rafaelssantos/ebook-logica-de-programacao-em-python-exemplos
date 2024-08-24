n = int(input("Informe a quantidade de números da sequência: "))
soma = 0        # O valor 0 é elemento neutro da soma
for e in range(n):
    soma = soma + e   # Alternativamente: soma += e
print("A soma dos", n, "primeiros números naturais é", soma)
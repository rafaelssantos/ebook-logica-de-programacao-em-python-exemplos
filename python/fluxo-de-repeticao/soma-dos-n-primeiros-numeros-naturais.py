n = int(input("Informe a quantidade de números da sequência: "))
soma = 0        # O valor 0 é elemento neutro da soma
for i in range(n):
    soma += i   # Equivalente a soma = soma + i
print("A soma dos", n, "primeiros números naturais é", soma)
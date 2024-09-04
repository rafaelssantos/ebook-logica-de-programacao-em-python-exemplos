n = int(input("Informe a quantidade de números da sequência: "))
produto = 1                     # O valor 1 é elemento neutro da multiplicação
for e in range(1, n + 1):
    produto = produto * e       # produto *= e
print("O produto dos", n, "primeiros números naturais é", produto)
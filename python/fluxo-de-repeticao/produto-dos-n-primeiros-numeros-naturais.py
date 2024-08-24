n = int(input("Informe a quantidade de números da sequência: "))
produto = 1        # O valor 1 é elemento neutro da multiplicação
for i in range(1, n + 1):
    produto = produto * i   # Alternativamente: produto *= i
print("O produto dos", n, "primeiros números naturais é", produto)
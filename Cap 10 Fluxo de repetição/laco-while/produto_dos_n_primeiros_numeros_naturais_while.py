n = int(input("Informe a quantidade de números da sequência: "))
produto = 1        # O valor 1 é elemento neutro da multiplicação

i = 1
while i <= n:
    produto = produto * i   # Alternativamente produto *= i
    i = i + 1               # i += 1
print("O produto dos", n, "primeiros números naturais é", produto)
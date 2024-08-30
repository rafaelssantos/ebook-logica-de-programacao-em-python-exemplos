a = 3
resultado = 0

for e in range(5):
    if e >= a:
        resultado = resultado * e
    else:
        resultado = resultado + e

print("resultado =", resultado)
print("a =", a)
print("i =", e)
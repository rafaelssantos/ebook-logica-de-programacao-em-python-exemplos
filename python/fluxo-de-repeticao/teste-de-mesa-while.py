a = 5
resultado = 0
i = 0

while i < 10:
    if i >= a:
        resultado = resultado * i
    else:
        resultado = resultado + i
    i = i + 2

print("resultado =", resultado)
print("a =", a)
print("i =", i)
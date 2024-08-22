a = 3
resultado = 0

for i in range(5):
    if i >= a:
        resultado *= i
    else:
        resultado += i

print("resultado =", resultado)
print("a =", a)
print("i =", i)
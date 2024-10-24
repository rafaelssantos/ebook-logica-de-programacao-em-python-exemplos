i = 0   # Evita loop infinito
while i < 10:
    i = i + 1   # Evita loop infinito
    if i % 2 == 0:
        continue
    print(i)
    
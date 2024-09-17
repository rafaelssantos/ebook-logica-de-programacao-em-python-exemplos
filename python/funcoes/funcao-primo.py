def e_primo(num):
    cont_divisores = 0

    for e in range(1, num + 1):
        if num % e == 0:
            cont_divisores = cont_divisores + 1
        if cont_divisores >= 3:
            break

    if cont_divisores == 2:
        return True
    else:
        return False


n = int(input("Deseja encontrar os números até qual número? "))
for e in range(2, n + 1):
    if e_primo(e):
        print(e)
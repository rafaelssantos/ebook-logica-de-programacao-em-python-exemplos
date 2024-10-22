def eh_primo(num):
    """
	Função que determina se um número é primo.
    Args:
		num (int): Número inteiro
	Returns:
		bool: True se primo e False se não for primo.
    """
    divisores = 0
    for e in range(1, num + 1):
        if num % e == 0:
            divisores = divisores + 1
    
    if divisores > 2:
        return False
    else:
        return True

# -------------------------------------------------------------
n = int(input("Informe o valor de n: "))
primos = [] # Lista vazia para armazenar os números primos

for e in range(2, n + 1):
    if eh_primo(e):
        primos.append(e)

print(primos)
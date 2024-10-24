# Solicita ao usuário para inserir uma string
texto = input("Digite uma string: ")

# Substitui as vogais 'a' e 'e' usando o método replace
resultado = texto.replace('a', '$').replace('e', '#')

# Exibe a string resultante
print("String codificada:", resultado)
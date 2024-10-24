n = int(input("Quantos verbetes você deseja inserir? "))

verbetes = []
for e in range(n):
    verbete = {}
    verbete["termo"] = input("Informe o termo: ")
    verbete["definição"] = input("Informe a definição: ")
    verbetes.append(verbete)

print(verbetes)

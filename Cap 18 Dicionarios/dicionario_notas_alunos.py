n = int(input("Qual a quantidade de alunos? "))

alunos = []

for e in range(n):
    aluno = {}
    aluno["nome"] = input("Informe o nome do aluno: ")
    aluno["nota"] = float(input("Informe a nota do aluno: "))
    alunos.append(aluno)

print("Lista de alunos")
print(alunos)

soma = 0
for aluno in alunos:
    soma = soma + aluno["nota"]

media = soma / len(alunos)
print("A média da turma é", media)
time_A = set(input("Informe os jogadores do time A separados por vírgula: ").split(sep=","))
time_B = set(input("Informe os jogadores do time B separados por vírgula: ").split(sep=","))
time_C = set(input("Informe os jogadores do time C separados por vírgula: ").split(sep=","))
time_D = set(input("Informe os jogadores do time D separados por vírgula: ").split(sep=","))

jogadores_inscritos = time_A | time_B | time_C | time_D
# Ou
jogadores_inscritos = time_A.union(time_B).union(time_C).union(time_D)

print("Jogadores inscritos no campeonato:", jogadores_inscritos)
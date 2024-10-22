nomes = ["André", "Bruno", "Carlos", "Daniela", "Eduarda", "Fernanda", "Gabriel", "Heloísa", "Isabela", "João"]

ponto_de_corte = int(input("Informe o ponto de corte: "))
nomes1 = nomes[:ponto_de_corte]
nomes2 = nomes[ponto_de_corte:]

print("Lista 1:", nomes1)
print("Lista 2:", nomes2)
# Módulo main.py

from saude import calula_imc # Importa a função imc do módulo saude

peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura? "))
imc = calula_imc(peso, altura)

print("O seu IMC é", imc)
def saudacao_personalizada2(nome1 = "Fulano", nome2 = "Beltrano"):
    print("Hello,", nome1, "e", nome2, "!")

# ---------------------------------------------------------

print("Estamos aprendendo a usar funções!")
alguem1 = "Albert  Einstein"
alguem2 = "Alan Turing"
saudacao_personalizada2(alguem1, alguem2)               # Posicionados
saudacao_personalizada2(nome2=alguem2, nome1=alguem1)   # Nomeados
print("Continuação do programa após a execução da função.")
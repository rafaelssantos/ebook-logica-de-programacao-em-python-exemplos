conta_bancaria = {}

conta_bancaria["Agencia"] = input("Informe o número da agência: ")
conta_bancaria["CC"] = input("Informe o número da conta_corrente: ")
conta_bancaria["Titular"]= input("Informe o nome completo do titular: ")
conta_bancaria["Saldo"] = float(input("Informe o saldo inicial: "))

print(conta_bancaria)
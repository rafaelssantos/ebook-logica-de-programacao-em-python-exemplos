import struct

peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / altura ** 2

caminho = input("Informe o caminho do arquivo: ")

with open(caminho, "wb") as arq:
    arq.write(struct.pack("f", peso))  # "f" indica um float
    arq.write(struct.pack("f", altura))  # "f" indica um float
    arq.write(struct.pack("f", imc))  # "f" indica um float
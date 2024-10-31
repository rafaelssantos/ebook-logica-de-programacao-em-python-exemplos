import struct

numero = 42  # Número inteiro a ser escrito
with open("numeros.bin", "wb") as arq:
    arq.write(struct.pack('i', numero))  # 'i' indica um inteiro
import struct

numero = 42  # int a ser escrito
with open("numeros.bin", "wb") as arq:
    arq.write(struct.pack("i", numero))  # "i" indica o tipo int
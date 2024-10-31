import struct

novo_numero = 100  # Número inteiro a ser anexado
with open("numeros.bin", "ab") as arq:
    arq.write(struct.pack('i', novo_numero))  # 'i' indica um inteiro
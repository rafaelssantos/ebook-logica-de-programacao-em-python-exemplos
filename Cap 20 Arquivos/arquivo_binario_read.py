import struct

with open("numeros.bin", "rb") as arq:
    while True:
        bloco = arq.read(4)  # Lê 4 bytes do arquivo

        if not bloco:   # Fim do arquivo
            break
        
        numero = struct.unpack('i', bloco)[0]  # 'i' indica um inteiro
        print(numero)
def funcao1():
    print("Hello, World em função!")

def funcao2(a):
    print(a)

def funcao3 (a : str, b):
    return a * b

def funcao4 (a, b, c) -> int:
    a = b - c
    return "Olá1", "Olá"

a = 5
b = 4
c = 3

d, e = funcao4 (a, b, c)
print(d, e)




# WHILE AULA 03

# Usando o BREAK
"""
x = 1
while x < 10:
    if x == 3:
        x = x + 1
        print("Achei o 3")
        break
    print(x)
    x = x + 1
print("FIM!")
"""

# USANDO CONTINUE
"""
x = 1
while x < 10:
    if x == 3:
        x = x + 1
        continue
    print(x)
    x = x + 1
print("FIM!")
"""

"""
x = 0
while x < 10:
    y = 0

    while y < 5:
        print(f"{x}, {y}")
        y += 1
    x += 1
"""

### Calculadora
"""
while True:
    print()
    n1 = input("Digite um número: ")
    n2 = input("Digite um número: ")
    operador = input("Digite um operador: ")

    opcao = input("Deseja sair? S / N ")
    if opcao == "s":
        break

    if not n1.isnumeric() or not n2.isnumeric():
        print("Voce precisa digitar um número")
        continue
    n1 = float(n1)
    n2 = float(n2)

    if operador == "+":
        print(n1 + n2)
    elif operador == "-":
        print(n1 - n2)
    elif operador == "*":
        print(n1 * n2)
    elif operador == "/":
        print(n1 / n2)
    else:
        print("Operador inválido")
"""

while True:
    print()
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    operador = input("Digite um operador: + - / * ")
    sair = input("Para sair pressione 's' ")
    if sair == "s":
        break

    if not n1.isnumeric() or not n2.isnumeric():
        print("Você precisa digitar um número")
        continue
    n1 = float(n1)
    n2 = float(n2)

    if operador == "+":
        print(n1 + n2)
    elif operador == "-":
        print(n1 - n2)
    elif operador == "*":
        print(n1 * n2)
    elif operador == "/":
        print(n1 / n2)
    else:
        print("Operador inválido")

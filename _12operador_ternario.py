"""
Operador ternário
"""
# OPERADOR TERNÁRIO
logged_user = False
msg = "Usuario logado" if logged_user else "Precisa fazer login"
print(msg)

print("-------------------------------------")

idade = input("Digite a sua idade: ")
if not idade.isnumeric():
    print("Você precisa digitar um número")
else:
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = "Pode acessar" if e_de_maior else "Não pode acessar"
    print(msg)



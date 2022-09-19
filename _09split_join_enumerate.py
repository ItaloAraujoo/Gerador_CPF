"""
SPLIT - DIVIDIR UMA STRING
JOIN - JUNTAR UMA LISTA
ENUMERATE - ENUMERAR ELEMENTOS DA LISTA
"""
# ENUMERATE
lista = ["Italo", "Paulo", "Maria"]
for indice, nome in enumerate(lista):
    print(indice, nome)

lista2 = ["Maura", "Lucas", "Larissa"]
n1 ,n2, n3 = lista2
print(n3)

# JOIN
# string = "O brasil é o pais da copa copa"
# lista = string.split(" ")
# string2 = 'Olá brasil'.join(lista)
# print(string2)

# palavra = ''
# contagem = 0
# for valor in lista:
#     qtd_vezes = lista.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
# print(palavra)


# Deixa todas as primeiras letras em maiusculo
# for valor in lista:
#     print(valor.strip().capitalize())


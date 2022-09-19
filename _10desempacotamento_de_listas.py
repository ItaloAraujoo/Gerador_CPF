"""
Desempacotamento de listas
"""

lista = ["Italo", "João", "Thiago", 1, 2, 3, 4]
n1, n2, *outra_lista, ultimo_lista = lista
print(ultimo_lista)
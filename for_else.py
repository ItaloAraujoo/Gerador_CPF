"""
FOR / ELSE EM PYTHON
"""

# Com o lower o python não vai se importar se a letra é maiuscula ou minuscula,
# ele trará o resultado de qualquer forma
variavel = ["Italo", "Amanda", "Maria"]
for valor in variavel:
    if valor.lower().startswith('i'):
        print("Começa com I", valor)
    else:
        print("Não começa", valor)

"""
FOR IN EM PYTHON
ITERANDO STRINGS COM FOR

FUNÇÃO RANGE(START=0, STOP, STEP=1)
"""

# FOR
# texto = "Python"
# for n, letra in enumerate(texto):
#     print(n, letra)

for numero in range(0, 24, 3):
    print(numero)

print("###########")

for n in range(80):
    if n % 8 == 0:
        print(n)

print("############")

texto = "python"
novaString = ''

for letra in texto:
    if letra == 'y':
        novaString = novaString + letra.upper()
    elif letra == 'o':
        novaString += letra.upper()
    else:
        novaString += letra
print(novaString)


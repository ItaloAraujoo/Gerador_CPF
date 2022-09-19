# Iterando strings com while

# frase = "O rato roeu a roupa do rei de roma"
# tamanhoFrase = len(frase)
# contador = 0
# novaString = ''
# inputUsuario = input('Qual letra deseja colocar maiuscula? ')
#
# ## ITERAÇÃO ##
# while contador < tamanhoFrase:
#     letra = frase[contador]
#     if letra == inputUsuario:
#         novaString += inputUsuario.upper()
#     else:
#         novaString += letra
#     contador += 1
# print(novaString)


frase = "Ola mundo, como vai?"
tamanhoFrase = len(frase)
contador = 0
novaString = ''
inputUsuario = input("Digite uma letra: ")

while contador < tamanhoFrase:
    letra = frase[contador]
    if letra == inputUsuario:
        novaString += inputUsuario.upper()
    else:
        novaString += letra
    contador += 1
print(novaString)








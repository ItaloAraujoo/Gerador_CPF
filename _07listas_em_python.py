"""
Listas em python
fatiamento
append, insert, pop, del, clear, extend
min, max
range
"""
import random

lista = ["maça", "uva", "abacaxi"]
# Alterando o indice 1
lista[1] = "morango"
print(lista[1])

# Vai pegar do indice 2 pra trás
lista2 = ["Martelo", "Carro", "Moto", "Navio"]
print(lista2[:2])

# Vai pegar do indice 2 pra frente
lista3 = ["Martelo", "Carro", "Moto", "Navio"]
print(lista3[2:])

# pegando o ultimo item da lista
lista4 = ["Italo", "Leandro", "Marcia", "Rafaela"]
print(lista4[-1])

# usando o extend
l5 = [1, 2, 3, 4]
l6 = [5, 6, 7, 8]
l5.extend(l6)
print(l5)

# usando o insert
l7 = [1, 2, 3, 4]
l7.insert(2, "Italo")
print(l7)

# usando o pop para excluir o ultimo indice
l7.pop()
print(l7)

# usando del para excluir uma parte da lista ou a lista inteira
l8 = [10, 20, 30, 40, 50, 60, 70]
del (l8[3:])
print(l8)

l9 = [1,2,3,4,5,6,7,8,9]
soma = 0
for valor in l9:
    soma = soma + valor
    print(soma, valor)

###############################################

# secreta = 'perfume'
# digitadas = []
# chances = 3
#
# while True:
#     if chances < 1:
#         print(f"Você perdeu!")
#         break
#
#     letra = input("Digite uma letra: ")
#     if len(letra) > 1:
#         print("Digite apenas uma letra")
#         continue
#
#     digitadas += letra
#     if letra in secreta:
#         print(f"A letra {letra} existe na palavra secreta")
#     else:
#         print(f"A letra {letra} não existe na palavra secreta")
#         digitadas.pop()
#
#     secreto_temporario = ''
#     for letra_secreta in secreta:
#         if letra_secreta in digitadas:
#             secreto_temporario += letra_secreta
#         else:
#             secreto_temporario += '*'
#
#     if secreto_temporario == secreta:
#         print(f"Você ganhou! A palavra secreta é {secreto_temporario}")
#         break
#     else:
#         print(f"A palavra secreta está assim: {secreto_temporario}")
#
#     if letra not in secreta:
#         chances -= 1
#         print(f"Você ainda tem {chances} chances")


# secreto = "goiaba"
# digitadas = []
# chances = 3
#
# while True:
#     print("A dica é: FRUTAS")
#
#     if chances < 1:
#         print("Você perdeu!")
#         break
#
#     # 1- Aqui pedimos para o usuario digitar uma letra e verificamos se o que ele digitou é menor que 2 letras.
#     letra = input("Digite uma letra: ")
#     if len(letra) < 1:
#         print("Digite apenas uma letra")
#         continue
#
#     digitadas += letra
#     # 2- Aqui se a letra estiver dentro da palavra secreta vai ser exibida uma mensagem dizendo que ele acertou a letra
#     if letra in secreto:
#         print("A letra secreta existe na palavra secreta")
#     else:
#         print("A letra não existe na palavra secreta")
#         digitadas.pop()
#
#     # Aqui tivemos que criar uma variavel vazia para ir fazendo a verificação e acrescentando cada letra correta dentro dessa nova variavel.
#     secreto_temporario = ''
#     for letra_secreta in secreto:
#         if letra_secreta in digitadas:
#             secreto_temporario += letra_secreta
#         else:
#             secreto_temporario += '*'
#
#     # Aqui faremos a verificação se o usuario ganhou o jogo
#     if secreto_temporario == secreto:
#         print(f"Você ganhou! A palavra secreta é {secreto_temporario}")
#         break
#     else:
#         print(f"A palavra secreta está assim: {secreto_temporario}")
#
#     # Aqui cada vez que o usuario errar uma letra iremos diminuir as chances dele no jogo
#     if letra not in secreto:
#         chances -= 1
#         print(f"Você ainda tem {chances} chances")


secreta = "pizza"
digitadas = []
chances = 3

# 1- Aqui pedimos para o usuario digitar uma letra e verificamos se o que ele digitou é menor que 2 letras.
while True:
    if chances < 1:
        print(f"GAME OVER")
        break

    letra = input("Digite uma letra: ")
    if len(letra) < 1:
        print("Digite apenas uma letra")
        continue

    digitadas += letra
# 2- Aqui se a letra estiver dentro da palavra secreta vai ser exibida uma mensagem dizendo que ele acertou a letra
    if letra in secreta:
        print(f"A letra {letra} existe na palavra secreta")
    else:
        print("A letra não existe na palavra secreta")
        digitadas.pop()
# 3- Aqui tivemos que criar uma variavel vazia para ir fazendo a verificação e acrescentando cada letra correta dentro dessa nova variavel.
    secreta_temporaria = ''
    for letra_secreta in secreta:
        if letra_secreta in digitadas:
            secreta_temporaria += letra_secreta
        else:
            secreta_temporaria += "*"
# 4- Aqui faremos a verificação se o usuario ganhou o jogo
    if secreta_temporaria == secreta:
        print(f"Parabens você ganhou o jogo! A palavra secreta é {secreta_temporaria}")
    else:
        print(f"A palavra secreta está assim: {secreta_temporaria}")
# 5- Aqui cada vez que o usuario errar uma letra iremos diminuir as chances dele no jogo
    if letra not in secreta:
        chances -= 1
        print(f"Você ainda tem {chances} chances")
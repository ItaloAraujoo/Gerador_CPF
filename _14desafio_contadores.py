"""
Exibir os valores dessa maneira:
for / while
0   10
1   9
2   8
3   7
4   6
5   5
6   4
7   3
8   2
"""

# minha solução:
numeros = 11
for valor in range(0, 9):
    numeros -= 1
    print(valor, numeros)

print("-----------------------")

# solução do professor:
for p,r in enumerate(range(10, 1, -1)):
    print(p, r)
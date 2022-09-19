# Formatando valores em python

# :s - texto (strings)
# :d - Inteiros
# :f - Numero de ponto flutuantes (float)


num1 = 10
num2 = 3
divisao = num1 / num2
print(f"Resultado: {divisao:.2f}")

# Utilizando format
nome = "Italo"
sobrenome = "Araujo"
nome_formatado = '{0} {1}'.format(nome, sobrenome)
print(nome_formatado)


"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Mara Campos'
idade = 58
altura = 1.58
peso = 67
ana_atual = 2022
nascimento = ana_atual - idade
imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos e pesa {peso} Kg')
print(f'O IMC de Mara Campos é {imc:2f}')
print(f'Mara nasceu em {nascimento}')

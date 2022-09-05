"""
Iniciar com letra, pode conter números, separar_, letras minúsculas
"""
nome = 'Evelyn'
print(nome, type(nome))
nome = 'Evelyn Campos'
idade = 23  # Int
altura = 1.64  # Float
e_maior = idade > 18  # Bool
peso = 64
imc = peso / (altura ** 2)

print('Nome', nome)
print('Idade', idade)
print('Altura', altura)
print('É maior', e_maior)
print(idade * altura)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)

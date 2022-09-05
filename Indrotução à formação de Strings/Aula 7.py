nome = 'Evelyn'
print(nome, type(nome))

nome = 'Evelyn Campos'
idade = 23  # Int
altura = 1.64  # Float
e_maior = idade > 18  # Bool
peso = 64
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:2f}')
print('{n} tem {i} anos e seu imc é {c}'. format(n=nome, i=idade, c=imc))

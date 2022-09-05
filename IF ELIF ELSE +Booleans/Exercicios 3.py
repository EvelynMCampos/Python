"""
Operadores Ralacionais
== > >= < <= !=

== Idaldade > maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""

num_1 = 2  # int
num_2 = 4  # int

expressao = (num_1 <= num_2)

print(expressao)

# Funciona com variáveis também


nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

# Limite para pegar emprestimo
idade_limite = 18

if idade >= idade_limite:
    print(f'{nome} pode pegar o emprestimo.')
else:
    print(f'{nome} NÃO pode pegar emprestimo.')

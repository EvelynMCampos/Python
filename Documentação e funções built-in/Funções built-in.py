"""
Criando uma calculadora
"""

num1 = input('Digite um número: ')
num2 = input('Digite outro número: ')

try:
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)
except:
    print('ERROR')

# isnumeric isdigit isdecimal
# números e positivos (12544122)

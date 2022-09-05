
usuario = input('Nome de usuario: ')
senha = input('Senha do usuário: ')

usuario_bd = 'Evelyn'
senha_bd = '45673'

if usuario_bd and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválido.')

# O bloco elif é usado quando se faz necessário checar outras condições ou variações da mesma condição. O bloco elif depende do bloco if, ou seja,
# é necessário primeiro usar o bloco if e somente se a expressão do bloco if for falsa, o bloco elif será verificado.

# O bloco else só é executado quando nenhuma condição de if ou elif for verdadeira. Por isso,
# quando precisamos de um valor padrão ou de uma resposta contrária à condição, é necessário adicionar o bloco else.
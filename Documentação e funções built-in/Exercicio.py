

numero_inteiro = input('Digite um número inteiro: ')

if not numero_inteiro.isdigit():
    print('Isso não é um número inteiro')

else:
    numero_inteiro = int(numero_inteiro)

    if not numero_inteiro % 2 == 0:
        print(f'{numero_inteiro} é par')
    else:
        print(f'{numero_inteiro} é impar')

# Horario

horario = input('Digite um horário (0-23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print("Horario deve estar entre 0 e 23")
    else:
        if horario < 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa noite!')
else:
    print("Por favor, digite um horario entre 0 e 23.")

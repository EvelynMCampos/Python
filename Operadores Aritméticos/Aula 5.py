"""
+, -, /, //, **, %, ()
"""
print('Multiplicação * ', 10 * 10)
print('Adição + ', 10 + 10)
print('Subtração - ', 10 - 5)
print('Divisão / ', 10 / 2)

print('Multiplicação * ', 10 * 'Evelyn')
print('Evelyn' + ' ' + 'Emi e ela tem '+ str(33) + 'anos')

print(10.5 // 3)
print(10 / 3)
print(10 % 5)
print(10 % 3)  # Resto da divição

print(5+2*10)
print((5+2)*10)  # Parentes para alterar a soma complexas

print(20*'A')
print(20*2)
print('20'+'A')
print(20+2)

(n + n) # Os parenteses tem a maior procedencia, contas dentro deles são realizadas primeiro
** # Depois vem a exponenciação
* / // % # Na sequencia multiplicação, divisão, divisão inteira e módulo
+ - # Por fim, some e subtração
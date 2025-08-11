print('Comparação de dois números')
print('-' * 20)
n = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print('-' * 20)

if n < n2:
    print(f'O maior número é: {n2}')
elif n > n2:
    print(f'O maior número é: {n}')
else:
    print('Os números são iguais!')
    
n = str(input('Digite o número que gostaria de converter: '))
opcao = int(input('''Digite para converter:
 [ 1 ] para BINÁRIO 
 [ 2 ] para OCTAL 
 [ 3 ] para HEXADECIMAL '''))
if opcao == 1:
    print(f'O número {n} convertido para binário é: {bin(n)}')
elif opcao == 2:
    print(f'O número {n} convertido para octal é: {oct(n)}')
elif opcao == 3:
    print(f'O número {n} convertido para hexadecimal é: {hex(n)}')
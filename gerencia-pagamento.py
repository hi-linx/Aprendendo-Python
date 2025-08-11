print(f'{'Lojinha Python':=^30}')
valor = float(input('Digite o valor de sua compra: '))
print('-' * 25)
opcao = int(input(''' Selecione a forma de pagamento:
[ 1 ] À vista em dinheiro
[ 2 ] À vista em cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
'''))

print('=' * 25)
if opcao == 1:
    print(f'Sua compra de R${valor} vai custar R${valor - (valor *0.1)} com desconto de 10% em dinheiro/cheque')
elif opcao == 2:
    print(f'Sua compra de R${valor} custará R${valor - (valor *0.05)} com desconto de 5% no cartão')
elif opcao == 3:
    print(f'Sua compra de R${valor} será dividida em duas parcelas de {valor/2} ')
elif opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    print(f'A compra foi dividida no cartão em {valor/(parcela + (parcela * 0.2)):.2f}')
# Quantidade de dias alugados, de km rodados
# Calculo do preço a pagar sendo que o carro custa R$60 o R$0,15 por km rodado

dia = int(input('Quantos dias o carro foi alugado?'))
carro = (60 * dia)

km = float(input('Quantos km rodados? '))
total =(carro + (km * 0.15))

print(f' O carro foi alugado por {dia} \n Ele teve um total de {km}Km rodados')
print(f'O valor total do aluguel do carro deu: {total}R$')
# Ler o comprimento do cateto oposto e do adjacente de um triangulo retangulo e mostrar o comprimento da hipotenusa

from math import sqrt, pow
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = sqrt(pow(co, 2) + pow(ca, 2))

print(f'Cateto Oposto: {co}, Cateto adjacente: {ca}, hipotenusa: {hipotenusa}')

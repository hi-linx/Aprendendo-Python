from math import pow

peso = float(input('Digite seu peso(Kg): '))
altura = float(input('Digite sua altura(m): '))
imc = peso/(pow(altura,2))

if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('Você está no PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE')
else:
    print('Você está com OBESIDADE MÓRBIDA, CUIDADO!')

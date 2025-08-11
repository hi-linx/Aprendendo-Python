from datetime import date

print('Classificando Atletas')
print('-' * 20)

ano = int(input('Digite o ano de seu nascimento: '))
idade = date.today().year - ano

if idade <= 9:
    print('Sua classificação é MIRIM')
elif idade <= 14:
    print('Sua classificação é INFANTIL')
elif idade <= 19:
    print('Sua classificação é JUNIOR')
elif idade <= 25:
    print('Sua classificação é SÊNIOR')
else:
    print('Sua classificação é MASTER')

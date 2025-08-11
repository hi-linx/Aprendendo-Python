nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))
m = (nota1 + nota2) / 2

if m < 5:
    print('O aluno está REPROVADO!')
elif m >= 5 and m < 6.9:
    print('O aluno está de RECUPERAÇÃO')
else:
    print('O aluno está APROVADO!')

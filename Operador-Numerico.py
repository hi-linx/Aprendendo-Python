# Potencia
r = 2**3
print(r)

# Divisão Inteira
a = 7//2
print(a)

#raiz quadrada -> **(1/2)
t = 25**(1/2)
print(t)

# Resto da divisão
m = 25%2

#nome = input('Digite seu nome: ')
#print(f'Olá {nome:=^20}!') # (^20 -> alinhamento centralizado em 20 espaços) (=^20 -> vai centralizar em 20 espaços
#colocando = em volta do nome

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

print(f'A soma entre {n1} e {n2} resulta em: {n1+n2}')
print(f'A potenciação entre \n {n1} e {n2} resulta em: {n1**n2}')
print(f'A divisão inteira entre {n1} e {n2} resulta em: {n1//n2}', end=' >>>') #o end='' nao vai dar quebra de linha
print(f' e o restante da divisão é {n1%n2}')
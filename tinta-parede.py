# Ler a largura e altura de uma parede em metros e calcular sua área e quantidade de tinta necessária para pintar ela
# Um litro de tinta pinta uma área de 2m²

l = float(input('Digite a largura: '))
h = float(input('Digite a altura: '))
a = l*h

print(f'A largura e a altura da parede é respectivamente: {l}m, {h}m')
print(f'A área da parede é: {a}m²', end=' ')
print(f'será necessário {a/2}l de tinta para pintar a parede ')
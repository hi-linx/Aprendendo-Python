# Ler um ângulo qualquer e mostrar o valor de seu seno, cosseno e tangente

import math
angulo = float(input('Digite um ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'O ângulo {angulo}, tem o valor do seno igual a {seno:.2f}')
print(f'O valor do cosseno é igual a {cosseno:.2f}, e o valor da tangente é igual a {tangente:.2f}')

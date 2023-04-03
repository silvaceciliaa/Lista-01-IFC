import math

lado = float(input('Digite o comprimento do lado: '))
nlados = float(input('Digite o número de lados: '))

area = (nlados * lado ** 2) / (4 * math.tan(math.pi / nlados))

print('Área do polígono regular:', area)


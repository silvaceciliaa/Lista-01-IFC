import math 
from math import sin, cos, sqrt, atan2

raio_terra = 6371.01

latitude1 = float(input('Digite a latitude do primeiro ponto: '))
longitude1 = float(input('Digite a longitude do primeiro ponto: '))
latitude2 = float(input('Digite a latitude do segundo ponto: '))
longitude2 = float(input('Digite a longitude do segundo ponto: '))

latitude1 = math.radians(latitude1)
latitude2 = math.radians(latitude2)
longitude1 = math.radians(longitude1)
longitude2 = math.radians(longitude2)

latitude = latitude2 - latitude1
longitude = longitude2 - longitude1

a = sin(latitude/2)**2 + cos(latitude1) * cos(latitude2) * sin(longitude/2)**2
c = 2 * atan2(sqrt(a), sqrt(1-a))

distancia = raio_terra * c

print('A distancia entre esses pontos é de aproximadamente:', distancia)
    
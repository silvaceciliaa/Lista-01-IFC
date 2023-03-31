import math

l1 = int(input('lado 1: '))
l2 = int(input('lado 2: '))
l3 = int(input('lado 3: '))

l = (l1 + l2 + l3) // 2

area = math.sqrt(l * (l - l1) * (l - l2) * (l - l3))

print('O valor da área é de:', area)
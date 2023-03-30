largura = int(input('Digite a largura em metros: '))
profundidade = int(input('Digite a profundidade em metros: '))

area = largura * profundidade 

hectares = area // 10000

print(hectares, 'hectares')
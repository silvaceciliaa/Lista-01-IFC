suco = float(input('Qual o valor do suco pedido? '))
pratoPrincipal = float(input('Qual o valor do prato principal? '))
sobremesa = float(input('Qual o valor da sobremesa? '))

valorComida = suco + pratoPrincipal + sobremesa
dezPorcento = valorComida * 0.10

valorTotal = valorComida + dezPorcento

print(f'O valor total é de: R${valorTotal:.2f}')
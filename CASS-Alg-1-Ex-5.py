vasilhameUserTipo1 = int(input('Quantos vasilhames de um litro ou menos você possui? '))
vasilhameUserTipo2 = int(input('Quantos vasilhames de mais de um litro você possui? '))

totalVasilhameTipo1 = 0.10 * vasilhameUserTipo1
totalVasilhameTipo2 = 0.25 * vasilhameUserTipo2

valorTotal = totalVasilhameTipo1 + totalVasilhameTipo2

print(f'O valor total de créditos é de: R${valorTotal:.2f}')
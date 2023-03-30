import math

a = int(input('Digite um número inteiro: '))
b = int(input('Digite outro número inteiro: '))

soma = a + b
diferenca = b - a
produto = a * b
quociente = a // b
resto = a % b
log = math.log10(a)
potencia = a ** b

print('A soma de a e b:', soma)
print('A diferença quando b é subtraído de a:', diferenca)
print('O produto de a por b:', produto)
print('O quociente quando a é dividido por b:', quociente)
print('O resto quando a é dividido por b:', resto)
print('O resultado de log10a:', log)
print('O resultado de a elevado a b:', potencia)

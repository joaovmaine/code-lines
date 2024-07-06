nome = 'João Victor Maine'
altura = 1.79
peso = 62
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura} de altura,'
linha_2 = f'pesa {peso} kg e seu imc é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)
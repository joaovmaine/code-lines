# receber um número
# receber um operador
# receber um outro número
# mostrar o resultado

print("Digite um número:")
num1 = float(input())
print("Digite um operador:")
operador = input()
print("Digite outro número:")
num2 = float(input())
print("Seu resultado é:")

if operador == '+':
    resultado = num1 + num2
    print(resultado)
elif operador == '-':
    resultado = num1 - num2
    print(resultado)
elif operador == '*':
    resultado = num1 * num2
    print(resultado)
elif operador == '/':
    resultado = num1 / num2
    print(resultado)
else:
    print("Operador incorreto.")

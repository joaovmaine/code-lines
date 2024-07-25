def contar_palavras(texto):
# Divide o texto em palavras usando espaços como delimitadores
    palavras = texto.split()
# Conta o número de palavras
    numero_de_palavras = len(palavras)
    return numero_de_palavras

# Solicitar texto ao usuário
texto_usuario = input('Digite o texto para a contagem: ')
# Conta as palavras do texto fornecido
resultado = contar_palavras(texto_usuario)
# Exibir resultado
print(f"O número de palavras no texto é: {resultado}")
def contar_caracteres(texto):
# Remove os espaços do texto
    texto_sem_espacos = texto.replace(" ", "")
# Conta o número de caracteres restantes
    numero_de_caracteres = len(texto_sem_espacos)
    return numero_de_caracteres

# Solicita ao usuário um texto
texto_usuario = input('Digite um texto para contar os caracteres (ignorar espaços): ')
# Contar os caracteres do texto fornecido
resultado = contar_caracteres(texto_usuario)
# Exibir resultado
print(f"O número de caracteres no texto (sem contar espaços) é: {resultado}")

def verificar_inicio():
    texto = input('Digite sua frase: ')
    if texto.lower().startswith('olá'):
        print(f'Olá, está contido na frase!')
    else:
        print(f"Olá, não está contido nessa frase, sua frase é: '{texto}'")

verificar_inicio()

def verify_par(a,b):
    soma = a + b
    if soma % 2 == 0:
        return f'A soma é dos valores é: {soma} e o resultado é par'
    else:
        return f'A soma é dos valores é: {soma} e o resultado é impar'
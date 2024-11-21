    




"""

#chama a soma
    a,b = obter_valores()
    result_soma = soma(a,b)
    print(f' O resultado da soma é: {result_soma}')

#chama a subtração
    a,b = obter_valores()
    result_subtracao = subtracao (a,b)
    print(f'O resultado da subtração é: {result_subtracao}')

#chama a divisao
    numerador, denomidaor = obter_valores()
    result_div = divisao(numerador,denomidaor)
    print(f'O resultado da divisão entre {numerador} e {denomidaor} é {result_div}')
    
"""
"""from pacote.multi import *
from pacote.verify_par import *
from pacote.sub import *


def obter_valores():
    valor1 = float(input("Digite o primeiro número:"))
    valor2 = float(input("Digite o segundo número:"))
    return valor1, valor2

def main():

    a = int(input("Digite um número: "))
    result_par = vericar_par(a)

    a,b = obter_valores()
    result_multi= multiplicar (a,b)
    print(f'O resultado da multiplicação é: {result_multi}')
    
    a,b = obter_valores()
    result_subtracao = subtracao (a,b)
    print(f'O resultado da subtração é: {result_subtracao}')

main()"""


"""soma = 0
with open('numeros.txt', 'r') as arquivo:
    for linha in arquivo:
        try:
            numero = int(linha.strip())  
            if numero % 3 == 0:
                soma += numero  
        except ValueError: 
            pass
print(soma)
"""

"""
import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

with open('numeros.txt', 'r', encoding='utf-8', errors='replace') as arquivo:  # adicionado encoding e errors
    for x in arquivo:
        x = x.strip()  
        x = remover_acentos(x)  
        if x.startswith('B'):
            print(x)
        elif x.endswith('o'):
            print(x)

"""
"""import unicodedata

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

with open('numeros.txt', 'r', CC, errors='replace') as arquivo:
    for x in arquivo:
        x = x.strip()
        x = remover_acentos(x)
        if x.startswith('B') and x.endswith('o'): 
            print(x)
"""

from pacote2.multi import *
from pacote2.verifica_par import *
from pacote2.sub import * 

def obter_valores():
    valor1 = float(input("Digite o seu primeiro valor: "))
    valor2 = float(input("Digite o seu segundo valor: "))
    return valor1,valor2

#chamando a subtração
a,b = obter_valores()
result_sub = sub(a,b)
print(f'o resultado da subtração é: {result_sub}')

#chamando a multiplicação
a,b = obter_valores()
result_multi = multi(a,b)
print(f'o resultado da multiplicação é: {result_multi}')

a,b = obter_valores()
result_soma_par = verify_par(a,b)
print(f'{result_soma_par}')



#--- Exercício 2  - Funções
#--- Escreva uma função que leia dois números do console
#--- Armazene cada número em uma variável
#--- Realize a divisão entre os dois números e armazene o resultado em uma terceira variável
#--- Imprima o resultado e uma mensagem usando f-string


'''SEMPRE lembrar de que o segundo numero não pode ser ZERO!!!!!'''

def leia_02_numeros():
    num1=int(input('NUMERO 1: '))
    num2=int(input('NUMERO 2: '))
    if num2 == 0:
        print('Impossível realizar divisão por zero!')
    else:
        result=num1/num2
        print(f'O resultado da divisão do nº {num1} pelo nº {num2} é {result}')
leia_02_numeros()
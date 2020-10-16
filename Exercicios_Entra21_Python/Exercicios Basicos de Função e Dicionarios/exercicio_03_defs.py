#--- Exercício 3  - Funções
#--- Crie uma função que leia três números float
#--- Armazene cada valor lido em uma variável
#--- Calcule a média entre os três números e armazene em uma quarta variável
#--- Imprima a média e uma mensagem usando f-string (módulo 3)

def leia_03_numeros_float():
    num1=float(input('NUMERO 1: '))
    num2=float(input('NUMERO 2: '))
    num3=float(input('NUMERO 3: '))
    media=(num1+num2+num3)/3
    print(f'A média entre os nºs {num1}, {num2} e {num3} é {media}')
leia_03_numeros_float()
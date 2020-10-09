#--- Exercício 5 - Funções
#--- Crie uma função para calculo de raiz
#--- A função deve ter uma variável que deternine qual é o indice da raiz(raiz quadrada, raiz cubica...)
#--- Leia um número do console, armazene em uma variável e passe para a função
#--- Realize o calculo da raiz e armazene em uma segunda variável e retorne 
#--- Imprima o resultado e uma mensagem usando f-string, fora da função

'teste'

# def calc_raiz():
#     indice=int(input('Qual o valor do indice? '))
#     num=int(input('Qual o numéro a ser calculado a raíz? '))
#     calc=num**(1/indice)
#     return calc
# print(f'O valor da raiz é {calc_raiz()}')

'aprendendo com artur'

num=int(input('Qual o numéro a ser calculado a raíz? '))

def calc_raiz(x):
    indice=int(input('Qual o valor do indice? '))
    calc=num**(1/indice)
    return calc

print(f'O valor da raiz é {calc_raiz(num)}')
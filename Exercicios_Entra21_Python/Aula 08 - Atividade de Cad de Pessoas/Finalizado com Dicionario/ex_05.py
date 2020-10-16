#--- Exercício 5  - Funções
#--- Escreva um programa para cadastro de pessoas e endereços:
#---o programa deve solicitar os dados de pessoa utilizados na função do ex1
#---o programa deve solicitar os dados de endereços utilizados na função do ex2
#---o programa deve passar o id obtido na função do ex1 para a função do ex2
#---o programa deve mostrar ao final os dados de todos as pessoas cadastradas com seus respectivos endereços utilizando as funções do ex3 e ex4

from ler_dados import ler_dados, ler_endereco

from ex_01 import cadastrar_pessoa
from ex_02 import cadastrar_endereco

from ex_03 import listar_pessoas, listar_pessoa_especifica
from ex_04 import listar_enderecos,  listar_endereco_epecifico

lista_pessoas = []

def main():

    while True:

        nome, sobrenome, idade = ler_dados()
        situacao_cadastro = cadastrar_pessoa(nome, sobrenome, idade, lista_pessoas)

        if type(situacao_cadastro) == int:
            rua, numero, complemento, bairro, cidade, estado = ler_endereco()
            cadastrar_endereco(situacao_cadastro, rua, numero, complemento, bairro, cidade, estado, lista_pessoas)
            
            x = input('\nPara continuar cadastrando digite Enter, para sair digite 0.\n')
            if x == '0':
                break
        else:
            print(situacao_cadastro + 'Tente novamente.')

    char = '*'
    print(f'{char*15} PESSOAS CADASTRADAS {char*15}')

    for pessoa in lista_pessoas:
        listar_pessoa_especifica(pessoa['id_usuario'], lista_pessoas)
        listar_endereco_epecifico( pessoa['id_usuario'], lista_pessoas)


main()
#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
# a função deve retornar um endereço cadastrado na função do ex2 filtrando por id da pessoa

from defs_p_cad_ex_03 import dados

def listar_enderecos() -> None:

    arquivo = open('lista_dados.txt','r')

    for linha in arquivo:
        elemento = linha.split(',')
        for i in range(len(elemento[4:])):
            print(f'{dados[i]}: {elemento[i]}')
    arquivo.close()

def listar_endereco_epecifico(id_usuario:str) -> None:
    
    arquivo = open('lista_dados.txt','r')

    for linha in arquivo:
        elemento = linha.split(',')
        if id_usuario in elemento:
            for i in range(len(elemento[4:])):
                print(f'{dados[i]}: {elemento[i]}')
    arquivo.close()


#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
# a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

def listar_pessoas(lista_pessoas:list) -> None:

    for pessoa in lista_pessoas:
        print(f'''
        Nome: {pessoa['nome']}
        Sobrenome: {pessoa['sobrenome']}
        Idade: {pessoa['idade']}''')


def listar_pessoa_especifica(id_usuario:int, lista_pessoas:list) -> None:

    for pessoa in lista_pessoas:
         if pessoa['id_usuario'] == id_usuario:
            print(f'''
    Nome: {pessoa['nome']}
    Sobrenome: {pessoa['sobrenome']}
    Idade: {pessoa['idade']}''')

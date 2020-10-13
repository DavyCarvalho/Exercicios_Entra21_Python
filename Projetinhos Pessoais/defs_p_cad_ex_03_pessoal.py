#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
# a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

'teste'
lista_pessoas = [{1:['davy','carvalho',21]},{2:['danyel','carvalho',17]}]

# def lista_pessoas_cadastradas():
#     return lista_pessoas

#print(f'{VAR:=^50}') colocando entre '='

def lista_pessoas_cadastradas():
    cabecalho_lista_clientes=('Lista de Pessoas Cadastradas')
    separacao='-'
    print(f'{cabecalho_lista_clientes:=^50}')
    for dicionario in lista_pessoas:
        for chave, valor in dicionario.items():
            print(f'''
            Nome: {valor[0]}
            Sobrenome: {valor[1]}
            Idade: {valor[2]}
            {separacao*20}
            ''')
    return('')

def pessoa_especifica(id_usuario:int):
    cabecalho_cliente_id=('Dados do Cliente Selecionado')
    print(f'{cabecalho_cliente_id:=^50}')
    for dicionario in lista_pessoas:
        for chave, valor in dicionario.items():
            if chave == id_usuario:
                return(f'''
                Nome: {valor[0]}
                Sobrenome: {valor[1]}
                Idade: {valor[2]}
                ''')

'teste'
print(pessoa_especifica(1))
print(lista_pessoas_cadastradas())
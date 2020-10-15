#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
# a função deve retornar um endereço cadastrado na função do ex2 filtrando por id da pessoa

def listar_enderecos_cadastrados():
    cabecalho_lista_enderecos=('Lista de Endereços Cadastrados')
    separacao='-'
    print(f'{cabecalho_lista_enderecos:=^50}')
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
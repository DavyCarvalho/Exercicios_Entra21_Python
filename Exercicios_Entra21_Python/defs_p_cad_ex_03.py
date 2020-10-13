#--- Exercício 3  - Funções
#--- Escreva uma função para listar pessoas cadastradas:
#---    a função deve retornar todas as pessoas cadastradas na função do ex1
#--- Escreva uma função para exibi uma pessoa específica:
# a função deve retornar uma pessoa cadastrada na função do ex1 filtrando por id

def listar_pessoas(lista_pessoas:list) -> None:
    cabecalho_lista_clientes=('Lista de Pessoas Cadastradas')
    separacao='-'

    print(f'{cabecalho_lista_clientes:=^50}')

    for pessoa in lista_pessoas:
        for chave, valor in pessoa.items():
            print(f'''
            Nome: {pessoa['nome']}
            Sobrenome: {pessoa['sobrenome']}
            Idade: {pessoa['idade']}
            {separacao*20}
            ''')

            
def listar_pessoa_especifica(id_usuario:int, lista_pessoas:list) -> None:
    cabecalho_cliente_id=('Dados do Cliente Selecionado')

    print(f'{cabecalho_cliente_id:=^50}')

    for pessoa in lista_pessoas:
        for chave, valor in pessoa.items():
            if chave == id_usuario:
                return(f'''
                Nome: {pessoa['nome']}
                Sobrenome: {pessoa['nome']}
                Idade: {pessoa['nome']}
                ''')
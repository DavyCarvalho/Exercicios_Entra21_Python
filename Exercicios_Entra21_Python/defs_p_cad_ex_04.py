#--- Exercício 4  - Funções
#--- Escreva uma função para listar endereços cadastrados:
#---    a função deve retornar todos os endereços cadastrados na função do ex2
#--- Escreva uma função para exibir um endereço específico:
# a função deve retornar um endereço cadastrado na função do ex2 filtrando por id da pessoa

def listar_enderecos(lista_pessoas:list) -> None:

    for pessoa in lista_pessoas:
        exibir_endereco(pessoa)


def listar_endereco_epecifico(user_id:int, lista_pessoas:list) -> None:
    
    for pessoa in lista_pessoas:
        if pessoa['id_usuario'] == user_id:
            exibir_endereco(pessoa)


def exibir_endereco(pessoa:dict) -> None:

    print(f'''
    Rua {pessoa['endereco']['rua']}, n° {pessoa['endereco']['numero']} - {pessoa['endereco']['complemento']}
    {pessoa['endereco']['bairro']}
    {pessoa['endereco']['cidade']} - {pessoa['endereco']['estado']}
    ''')
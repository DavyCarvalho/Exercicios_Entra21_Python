def ler_dados () -> str:
    conteudo_topo = ' CADASTRO DE PESSOAS - HBSIS '
    print(f'{conteudo_topo:=^50}')

    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    idade = int(input('Informe a idade: '))

    return nome, sobrenome, idade

def ler_endereco() -> str:

    conteudo_endereco = 'ENDEREÇO'
    print(f'\n{conteudo_endereco:*^50}')

    rua = input('Rua: ')
    numero = input('Número: ')
    complemento = input('Complemento: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')

    return rua, numero, complemento, bairro, cidade, estado
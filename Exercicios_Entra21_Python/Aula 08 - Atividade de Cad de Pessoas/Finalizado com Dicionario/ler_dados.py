def ler_dados () -> str:

    char = '*'
    print(f'{char*15} CADASTRO DE DADOS {char*15}')

    nome = input('Informe o nome: ')
    sobrenome = input('Informe o sobrenome: ')
    idade = int(input('Informe a idade: '))

    return nome, sobrenome, idade


def ler_endereco() -> str:

    char = '*'
    print(f'\n{char*15} ENDEREÇO {char*15}')

    rua = input('Rua: ')
    numero = input('Número: ')
    complemento = input('Complemento: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado: ')

    return rua, numero, complemento, bairro, cidade, estado


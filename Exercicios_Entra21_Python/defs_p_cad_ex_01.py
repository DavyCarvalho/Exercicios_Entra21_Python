#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

def cadastrar_pessoa(nome:str, sobrenome:str, idade:int, lista_pessoas:list):
    usuario = {}

    if idade < 18:

        return 'Ser humano menor de idade!'

    else:
        usuario['id_usuario'] = id(nome)
        usuario['nome'] = nome
        usuario['sobrenome'] = sobrenome
        usuario['idade'] = idade
        lista_pessoas.append(usuario)

        return id(nome)


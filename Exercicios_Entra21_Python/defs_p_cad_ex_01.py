#--- Exercício 1  - Funções
#--- Escreva uma função para cadastro de pessoa:
#---       a função deve receber três parâmetros, nome, sobrenome e idade
#---       a função deve salvar os dados da pessoa em uma lista com escopo global
#---       a função deve permitir o cadastro apenas de pessoas com idade igual ou superior a 18 anos
#---       a função deve retornar uma mensagem caso a idade informada seja menor que 18
#---       caso a pessoa tenha sido cadastrada com sucesso deve ser retornado um id 
#--- A função deve ser salva em um arquivo diferente do arquivo principal onde será chamada

def cadastrar_pessoa(nome:str, sobrenome:str, idade:int):
    
    if idade < 18:

        return 'Ser humano menor de idade!'

    else:
        arquivo = open('lista_dados.txt', 'a')
        arquivo.write(f"{str(id(nome))},{nome},{sobrenome},{idade}")
        arquivo.close()

        return str(id(nome))

# cadastrar_pessoa('DAVY','CARVALHO',21)

# 22354112,DAVY,CARVALHO,21,itajai,99,aaaa,aqui,de deus,sc
# 32132132,EDUARDA,TASCHETTO,98,itajai,789,bbbbb,la,de pessoas,RS

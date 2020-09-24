"""Exercício 4

(use o conhecimento que foi passado no curso)

Crie um programa com um menu interativo:

-----
Cadastro de pessoas v1.0

A) Cadastrar Pessoa
B) Ver todos os nomes cadastrados:
C) Ver cadastro pelo nome:
D) Apagar um cadastro pelo nome:
S) Sair

-----



Para A: Cadastre os dados do cliente (Nome, idade, sexo, telefone
Para B: Mostre todos os nomes dos clientes (só os nomes)
Para C: Digite o nome do cliente e mostre todos os dados dele.
Para D: Digite o nome do cliente e o apague do cadastro
Para S: Mostre uma mensagem de despedida e termine o programa
Para qualquer outro valor: Mostre "Opção invalida"
"""
# TESTE
# lista_nomes = ['DAVY', 'SAMUEL', 'DANYEL', 'EMILY']
# lista_idades = ['21', '22', '17', '19']
# lista_sexo = ['m', 'm', 'm', 'f']
# lista_telefone = ['9999', '8888', '7777', '4444']

lista_nomes = []
lista_idades = []
lista_sexo = []
lista_telefone = []

print('''
    ############################
    # Cadastro de pessoas v1.0 #
    ############################
''')
#######################################################################
opcao = ''

while not(opcao == 'S' or opcao == 's'):

    opcao = input('''
    Digite a opção desejada:

    A) Cadastrar Pessoa
    B) Ver todos os nomes cadastrados:
    C) Ver cadastro pelo nome:
    D) Apagar um cadastro pelo nome:
    S) Sair

    ''')
#######################################################################
    if opcao == 'A' or opcao == 'a':
        nome = input('Nome do cliente: ')
        if nome == '':
            while nome == '':
                print('Nome em branco, favor digitar um nome!')
                nome = input('Nome do cliente: ')
        elif nome.isdigit():
            while nome.isdigit():
                print('Não é aceito nome em numerais, favor digitar um nome!')
                nome = input('Nome do cliente: ')
        lista_nomes.append(nome.upper())
        idade = input('Idade do cliente:')
        if not(idade.isdigit()):
            while not(idade.isdigit()):
                print('Idade em branco ou valor inválido, favor digitar um novo valor!')
                idade = (input('Idade do cliente: '))
        lista_idades.append(idade)
        sex = input("Gênero do cliente: (Digite apenas 'F' ou 'M')")
        if sex != 'F' and sex != 'M' and sex != 'f' and sex != 'm':
            while True:
                print('Valor invalido para Gênero!')
                sex = input("Gênero do cliente: (Digite apenas 'F' ou 'M')")
                if sex == 'F' or sex == 'M' or sex == 'f' or sex == 'm':
                    break
        lista_sexo.append(sex.upper())
        fone = (input("Fone do cliente:"))
        if not(fone.isdigit()):
            while not(fone.isdigit()):
                print('Valor inválido, favor digitar um novo valor!')
                fone = input("Fone do cliente:")
        lista_telefone.append(fone)
#######################################################################
    if opcao == 'B' or opcao == 'b':
        print('''
        ##################################################
        ----------Lista de Clientes Cadastrados:----------
        ##################################################
        ''')
        print('\n')
        for i in range(len(lista_nomes)):
            print(f'''
            Nome: {lista_nomes[i]}
            --------------------------
            ''')
        continue
########################################################################
    elif opcao == 'C' or opcao == 'c':
        cliente_selecionado = input('Digitei o nome do cliente que você deseja exibir os dados: ')
        cliente_selecionado.upper()
        for i in range(len(lista_nomes)):
            if lista_nomes[i] == cliente_selecionado.upper():
                print(f'''
                Nome: {lista_nomes[i]}
                Idade: {lista_idades[i]}
                Gênero: {lista_sexo[i]}
                Contato: {lista_telefone[i]}
                ''')
        continue
#######################################################################
    elif opcao == 'D' or opcao == 'd':
        cliente_apagado_ok = False
        while cliente_apagado_ok == False:
            cliente_selecionado_apagar = input('Digitei o nome do cliente que você deseja EXCLUIR os dados: ')

            for i in range(len(lista_nomes)):
                if lista_nomes[i] == cliente_selecionado_apagar.upper():
                    print(f'''
                    Nome: {lista_nomes[i]}
                    Idade: {lista_idades[i]}
                    Gênero: {lista_sexo[i]}
                    Contato: {lista_telefone[i]}

                    DADOS DO CLIENTE COMPLETAMENTE APAGADOS!
                    ''')
                    lista_nomes.pop(i)
                    lista_idades.pop(i)
                    lista_sexo.pop(i)
                    lista_telefone.pop(i)
                    cliente_apagado_ok = True
                    break
            if cliente_apagado_ok == False:
                print(f'''
                    O cliente: '{cliente_selecionado_apagar}' 
                    não existe no nosso banco de dados, 
                    favor verificar o nome e digitar novamente!
                    ''')
                continue
#######################################################################
    elif opcao == 'S' or opcao == 's':
        print('Obrigado por usar nossos serviços! Volte sempre!')
#######################################################################
    else:
        print('Opção Invalida, Favor selecionar novamente!')
        continue
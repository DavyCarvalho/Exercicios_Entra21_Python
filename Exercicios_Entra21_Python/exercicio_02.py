#--- Exercício 2 - Variáveis
#--- Crie um menu para um sistema de cadastro de funcionários
#--- O menu deve ser impresso com a função format()
#--- As opções devem ser variáveis do tipo inteiro
#--- As descrições das opções serão:
#---    Cadastrar funcionário
#---    Listar funcionários
#---    Editar funcionário
#---    Deletar funcionário
#---    Sair
#--- Além das opções o menu deve conter um cabeçalho e um rodapé
#--- Entre o cabeçalho e o menu e entre o menu e o rodapé deverá ter espaçamento de 3 linhas
#--- Deve ser utilizado os caracteres especiais de quebra de linha e de tabulação

lista_opcoes = {'Cadastrar funcionário':1, 
            'Listar funcionários':2, 
            'Editar funcionário':3,
            'Deletar funcionário':4,
            'Sair':5
            }

a, b, c, d, e = lista_opcoes.values()
print('-'*40)
print('SISTEMA DE CADASTRO DE CLIENTES')
print('\n')
print("""
{}) Cadastrar funcionário
{}) Listar funcionários
{}) Editar funcionário
{}) Deletar funcionário
{}) Sair
""".format(a, b, c, d, e))
print('\n')
print('-'*40)
opcao = int(input('Digite a opção desejada: '))

for chave, valor in lista_opcoes.items():
    if opcao == valor:
        print('Voce selecionou a opção {}'.format(valor), 'referente a {}'.format(chave))
        print('Executando a função {}....'.format(chave))

#refeito com a ajuda do artur das trufa, gnt fina ele


#ERRADO - ESPERANDO CORREÇÃO DO PROFESSOR

# opcao = int(input('''
# !!! SISTEMA DE CADASTTRO DE CLIENTES !!!

# 1) Cadastrar funcionário
# 2) Listar funcionários
# 3) Editar funcionário
# 4) Deletar funcionário
# 5) Sair

# Digite a opção desejada: 
# '''))

# if opcao == 1:
#     print('Cadastrando funcionário...')
# elif opcao == 2:
#     print('Exibindo lista de funcionários...')
# elif opcao == 3:
#     print('Alterando cadastro de funcionário...')
# elif opcao == 4:
#     print('Apagando cadastro de funcionário...')
# elif opcao == 5:
#     print('Saindo...')

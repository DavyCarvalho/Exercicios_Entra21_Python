#--- Exercício 1  - Funções - 1
#--- Escreva uma função que imprima um cabeçalho
#--- O cabeçalho deve ser escrito usando a multiplicação de carácter
#--- O cabeçalho deev conter o nome de uma empresa, que será uma variável
#--- Realize a chamada da função na ultima linha do seu programa

def cabecalho():
        emp = 'AMBEV'
        print('='*10,'{} - CADASTRO DE CLIENTES'.format(emp),'='*10)
        #dica do artur
        #print(f'{emp:=^50}')
cabecalho()
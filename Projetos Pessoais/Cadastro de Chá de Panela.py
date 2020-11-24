from time import sleep
from os import system, name

print(f"{' CADASTRO DE CHÁ DE PANELA ':=^50}")

lista_pessoas = []

while True:
    
    try:
        opcao = int(input("""
Digite: 
1) Cadastrar pessoa na lista
2) Mostrar lista 
3) Sair do programa

"""))
        
        if opcao == 1:
            while True:
                try:
                    nova_pessoa = int(input("Digite 1 para sair ou A para adicionar uma pessoa à lista: "))
                    
                    print('Voltando ao MENU'), sleep(0.50)                  
                    system('cls')
                    break                    
                    
                except ValueError:
                    
                    pessoa = input("Digite o nome da Pessoa: ")
                                        
                    lista_pessoas.append(pessoa)
                    
                    print('Aguarde... '), sleep(0.50)
                    print('Carregando dados'), sleep(0.50)
                    print(f'DADOS CARREGADOS COM SUCECESSO!\n')
                    sleep(0.50)
                    
                    system('cls')
                    continue
                    
            
        elif opcao == 2:
            
            print('Aguarde'), sleep(0.50)
            print('Carregando dados'), sleep(0.50)
            print("==== PESSOAS CADASTRADAS ====")
            
            for posicao, pessoa in enumerate(lista_pessoas,1):
                print(f"{posicao}: {pessoa}")
                
            
                
        elif opcao == 3:
            print('Aguarde'), sleep(0.50)
            print('Obrigado por usar nosso serviço! Volte sempre!')
                
        
    except ValueError:
        print("Valor invalido!!! Tente Novamente!!!")
        sleep(0.5)
        continue
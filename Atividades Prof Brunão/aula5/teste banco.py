from veiculos import Pessoa


while True:
    try: 
        valor = int(input(
            """Digite a operação desejada
            1 - Cadastrar Pessoa
            2 - Cadastrar Conta
            3 - Visualizar Saldo
            4 - Fazer um depósito
            5 - Sair\n"""))

        if (valor not in range(1,6)):
            
            print("Valor inválido! Tente novamente.")
            continue
    
    except:
        print("Valor inválido! Tente novamente.")
        continue
    
    else:
    
        if valor == 1:
            
            with open("Clientes_Banco.txt", "a") as arquivo:
                nome = input("Insira o nome do cliente:\n").upper()
                idade = input("Insira a idade do cliente:\n")
                cpf = input("Insira o CPF do cliente:\n")
                saldo = 0
                
                arquivo.write(f"{nome};{idade};{cpf};{saldo}\n")
                                    
        if valor == 2:
            
            cliente = input("Qual cliente você "
                            "gostaria de criar uma conta?").upper()

            with open("Clientes_Banco.txt", "r") as arquivo:
                linhas_arquivo = arquivo.readlines()
                
                for lista_cliente in linhas_arquivo:
                    
                    if lista_cliente.strip().split(",")[0].upper() == cliente:
                        print("Achou")
                    
            
            banco = input("Em qual banco você deseja"
                            "cadastrar a conta do cliente?")
        

        if valor == 3:
            
            cliente_cpf = input("Digite seu CPF para " 
                                "verificar seu saldo!\n")
            
            with open("Clientes_Banco.txt", "r") as arquivo:
                linhas_arquivo = arquivo.readlines()
                
                for clientes in linhas_arquivo:

                    if clientes.strip().split(",")[2] == cliente_cpf:
                        print(f"Seu saldo atual é de R$ {clientes.strip().split(',')[2]}")
                    #   print(f"Seu saldo atual é de R$ {clientes.strip().split(',')[3]}")
                        
        if valor == 4:
            pass
        
        if valor == 5:
            print("Agradecemos a sua visita!")
            break

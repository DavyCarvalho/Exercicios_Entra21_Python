import sqlite3
from time import sleep
from os import system, name

class Proprietario():
        
        def __init__(self, nome_proprietario:str, cpf:str, idade:int):
                self.nome_proprietario = nome_proprietario
                self.cpf = cpf
                self.idade = idade
        
        
        def salvar_proprietario(self): # OK
                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                cursor = conn.cursor()
                
                tupla_dados_proprietario = (self.nome_proprietario,
                                            self.cpf, self.idade)
                
                cursor.execute("""
                               INSERT INTO proprietarios 
                               (nome_proprietario, cpf, idade)
                               VALUES (?,?,?)
                               """, tupla_dados_proprietario)
                conn.commit()
                conn.close()
                
                print(f"{' Proprietário Cadastrado com sucesso! ':=^50}")
                

        def excluir_proprietario(self):
                               
                while True:
                        cliente_selecionado = (input("Digite o ID do cliente que você deseja excluir o cadastro: "))
                        
                        if cliente_selecionado == int:
                                while True:
                                        confirmacao = input("")
                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                cursor = conn.cursor()
                                
                                break
                        else:
                                print("O valor da chave ID deve ser um numero!\n")
                                continue
                        
        
        def atualizar_proprietario(self): #OK
                while True:
                        
                        try:
                                opcao = int(input("Digite o ID do cliente que deseja atualizar ou "
                                                  "Tecle Enter para vizualizar todos os clientes!"))
                                
                                while True:
                                        
                                        conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                        cursor = conn.cursor()

                                        cursor.execute("""
                                        SELECT * FROM proprietarios;
                                        """)

                                        for pessoa in cursor.fetchall():
                                                dado = list(pessoa)
                                                if opcao in dado:
                                                        print(f"""
                                                        ===============================
                                                        ID CLIENTE: {dado[0]} - BLOQUEADO CONTRA ALTERAÇÕES
                                                        NOME: {dado[1]}
                                                        CPF: {dado[2]}
                                                        IDADE: {dado[3]}
                                                        CRIADO EM: {dado[4]} - BLOQUEADO CONTRA ALTERAÇÕES""")
                                                        conn.close()
                                                        break
                                                # TEM UM PROBLEMA AQUI !!!!! VERIFICAR !!!!
                                                else:
                                                        print("ID DE CLIENTE NÃO ENCONTRADO!!!"
                                                        "FAVOR DIGITE NOVAMENTE!")
                                                        continue
                                
                                colunas = ['NOME','CPF','IDADE']
                                
                                for coluna in range(1):
                                        print(f"""
                                              Opções de colunas:
                                              
                                              1){colunas[0]}
                                              2){colunas[1]}
                                              3){colunas[2]}
                                              """)
                                while True:
                                        try:
                                                coluna_alterar_tabela = int(input("Digite o Nº da coluna você deseja alterar na tabela PESSOAS?"))
                                                
                                                if coluna_alterar_tabela == 1:
                                                        
                                                        conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                        cursor = conn.cursor()
                                                                                        
                                                        nome_cliente = input("")

                                                        cursor.execute("""
                                                        UPDATE proprietarios
                                                        SET nome_proprietario = ?
                                                        WHERE id = ?
                                                        """, (nome_cliente, opcao))

                                                        conn.commit()

                                                        print('Nome atualizado com sucesso!')
                                                        break
                                                        
                                                elif coluna_alterar_tabela == 2:
                                                        
                                                        conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                        cursor = conn.cursor()
                                                                                        
                                                        cpf_cliente = input("")

                                                        cursor.execute("""
                                                        UPDATE proprietarios
                                                        SET cpf = ?
                                                        WHERE id = ?
                                                        """, (cpf_cliente, opcao))

                                                        conn.commit()

                                                        print('CPF atualizado com sucesso!')
                                                        break
                                                        
                                                elif coluna_alterar_tabela == 3:
                                                        
                                                        conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                        cursor = conn.cursor()
                                                                                        
                                                        idade_cliente = input("")

                                                        cursor.execute("""
                                                        UPDATE proprietarios
                                                        SET idade = ?
                                                        WHERE id = ?
                                                        """, (idade_cliente, opcao))

                                                        conn.commit()

                                                        print('IDADE atualizada com sucesso!')
                                                        break       
                                        except ValueError:
                                                print('Digite um valor valido!\n')
                                                continue
                                                           
                
                        except ValueError:
                                print("""===============================
                                                Pessoas Cadastradas      
                                         -------------------------------""")
                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                cursor = conn.cursor()

                                cursor.execute("""
                                SELECT * FROM proprietarios;
                                """)

                                for pessoa in cursor.fetchall():
                                        dado = list(pessoa)
                                        print(f"""
                                               ===============================
                                               ID CLIENTE: {dado[0]} - BLOQUEADO CONTRA ALTERAÇÕES
                                               NOME: {dado[1]}
                                               CPF: {dado[2]}
                                               IDADE: {dado[3]}
                                               CRIADO EM: {dado[4]} - BLOQUEADO CONTRA ALTERAÇÕES""")
                                conn.close()
                                continue                                
        
        
        def exibir_proprietario(self):# OK
                
                while True:
                                                
                        try:
                      
                                opcao = input("Digite o ID do cliente desejado ou "
                                              "Pressione Enter para ver os clientes cadastrados: ")

                                print("""===============================
                                                Pessoas Cadastradas      
                                         -------------------------------""")
                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                cursor = conn.cursor()

                                cursor.execute("""
                                SELECT * FROM proprietarios;
                                """)

                                for pessoa in cursor.fetchall():
                                        dado = list(pessoa)
                                        if opcao in dado:
                                                print(f"""
                                                ===============================
                                                ID CLIENTE: {dado[0]}
                                                NOME: {dado[1]}
                                                CPF: {dado[2]}
                                                IDADE: {dado[3]}
                                                CRIADO EM: {dado[4]}""")
                                                conn.close()
                                                break
                                        else:
                                                print("ID DE CLIENTE NÃO ENCONTRADO!!!"
                                                      "FAVOR DIGITE NOVAMENTE!")
                                                continue
                                                                
                        except ValueError:
                                
                                print("""===============================
                                                Pessoas Cadastradas      
                                         -------------------------------""")
                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                cursor = conn.cursor()

                                cursor.execute("""
                                SELECT * FROM proprietarios;
                                """)

                                for pessoa in cursor.fetchall():
                                        dado = list(pessoa)
                                        print(f"""
                                               ===============================
                                               ID CLIENTE: {dado[0]}
                                               NOME: {dado[1]}
                                               CPF: {dado[2]}
                                               IDADE: {dado[3]}
                                               CRIADO EM: {dado[4]}""")
                                conn.close()
                                break  
        
        
        def adicionar_coluna_proprietario(self):
                pass
        
        
        def remover_coluna_proprietario(self):
                pass
                
        
class Veiculo():

        def __init__(self, nome_veiculo:str, marca:str, categoria:str,
                           cor:str, tipo_motor:str, combustivel:str, ano:int,
                           num_portas:int, qtd_passageiros:int, placa:str): 
                self.nome_veiculo = nome_veiculo
                self.marca = marca
                self.categoria = categoria
                self.cor = cor
                self.tipo_motor = tipo_motor
                self.combustivel = combustivel
                self.ano = ano
                self.num_portas = num_portas
                self.qtd_passageiros = qtd_passageiros
                self.placa = placa
        
        
        def salvar_veiculo(self): # OK
                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                cursor = conn.cursor()


                tupla_dados_veiculo = (self.nome_veiculo, self.marca, self.categoria, 
                self.cor, self.tipo_motor, self.combustivel, self.ano, 
                self.num_portas, self.qtd_passageiros, self.placa)
                

                cursor.execute("""
                                INSERT INTO veiculos (nome_veiculo, marca, categoria, 
                                cor, tipo_motor, combustivel, ano, 
                                num_portas, qtd_passageiros, placa)
                                VALUES (?,?,?,?,?,?,?,?,?,?)
                                """, tupla_dados_veiculo)
                conn.commit()
                conn.close()

                print(f"{' Veículo cadastrado com sucesso ':=^50}")


        def excluir_veiculo(self):
                pass
                
        
        def atualizar_veiculo(self):
                while True:
                        
                        try:
                                while True:
                                        
                                        opcao = int(input("Digite o ID do veículo que deseja atualizar ou "
                                                  "Tecle Enter para vizualizar todos os veículos!"))
                                        
                                        conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                        cursor = conn.cursor()

                                        cursor.execute("""
                                        SELECT * FROM veiculos;
                                        """)

                                        for veiculo in cursor.fetchall():
                                                dado = list(veiculo)
                                                if opcao in dado:
                                                        print(f"""
                                                        ===============================
                                                        ID VEÍCULO: {dado[0]} - BLOQUEADO CONTRA ALTERAÇÕES
                                                        NOME VEÍCULO: {dado[1]}
                                                        MARCA: {dado[2]}
                                                        CATEGORIA: {dado[3]}
                                                        COR: {dado[4]}
                                                        TIPO DE MOTOR: {dado[5]}
                                                        COMBUSTÍVEL: {dado[6]}
                                                        ANO: {dado[7]}
                                                        Nº DE PORTAS: {dado[8]}
                                                        Nº DE PASSAGEIROS: {dado[9]}
                                                        PLACA: {dado[10]}
                                                        DATA DE CRIAÇÃO: {dado[11]} - BLOQUEADO CONTRA ALTERAÇÕES""")
                                                        conn.close()
                                                        break
                                                else:
                                                        print("ID DE VEÍCULO NÃO ENCONTRADO!!!"
                                                                "FAVOR DIGITE NOVAMENTE!")
                                                        continue
                                
                                colunas = ['NOME DO VEÍCULO','MARCA','CATEGORIA', 'COR', 
                                           'TIPO DO MOTOR', 'COMBUSTIVEL', 'ANO', 'NUMERO DE PORTAS',
                                           'QUANTIDADE DE PASSAGEIROS', 'PLACA']
                                
                                for coluna in range(1):
                                        print(f"""
                                        Opções de colunas:
                                        
                                        1){colunas[0]}   6){colunas[5]}
                                        2){colunas[1]}             7){colunas[6]}
                                        3){colunas[2]}         8){colunas[7]}
                                        4){colunas[3]}               9){colunas[8]}
                                        5){colunas[4]}     10){colunas[9]}
                                        """)
                                        while True:
                                                try:        
                                                        coluna_alterar_tabela = input("Digite o Nº da coluna você deseja alterar na tabela VEÍCULOS?")
                                                        
                                                        if coluna_alterar_tabela == 1:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                nome_veiculo = input("Digite o Nome atualizado: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET nome_veiculo = ?
                                                                WHERE id = ?
                                                                """, (nome_veiculo, opcao))

                                                                conn.commit()

                                                                print('Nome do veículo atualizado com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 2:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                marca = input("Digite a Marca atualizada: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET marca = ?
                                                                WHERE id = ?
                                                                """, (marca, opcao))

                                                                conn.commit()

                                                                print('Marca do veículo atualizada com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 3:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                categoria = input("Digite a Categoria atualizada: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET categoria = ?
                                                                WHERE id = ?
                                                                """, (categoria, opcao))

                                                                conn.commit()

                                                                print('Categoria do veículo atualizada com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 4:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                cor = input("Digite a Cor atualizada: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET cor = ?
                                                                WHERE id = ?
                                                                """, (cor, opcao))

                                                                conn.commit()

                                                                print('Cor do veículo atualizada com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 5:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                tipo_motor = input("Digite Tipo do motor atualizado: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET tipo_motor = ?
                                                                WHERE id = ?
                                                                """, (tipo_motor, opcao))

                                                                conn.commit()

                                                                print('Tipo do motor do veículo atualizado com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 6:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                combustivel = input("Digite o Combustível atualizado: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET combustivel = ?
                                                                WHERE id = ?
                                                                """, (combustivel, opcao))

                                                                conn.commit()

                                                                print('Combustível do veículo atualizado com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 7:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                ano = input("Digite o Ano atualizado: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET ano = ?
                                                                WHERE id = ?
                                                                """, (ano, opcao))

                                                                conn.commit()

                                                                print('Ano do veículo atualizado com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 8:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                num_portas = input("Digite o Número de portas atualizado: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET num_portas = ?
                                                                WHERE id = ?
                                                                """, (num_portas, opcao))

                                                                conn.commit()

                                                                print('Número de portas do veículo atualizado com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 9:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                qtd_passageiros = input("Digite o Quantidade de passageiros atualizada: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET qtd_passageiros = ?
                                                                WHERE id = ?
                                                                """, (qtd_passageiros, opcao))

                                                                conn.commit()

                                                                print('Quantidade de passageiros do veículo atualizado com sucesso!')
                                                                break
                                                        
                                                        elif coluna_alterar_tabela == 10:
                                                                
                                                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                                                cursor = conn.cursor()
                                                                                                
                                                                placa = input("Digite a Placa atualizada: \n")

                                                                cursor.execute("""
                                                                UPDATE veiculos
                                                                SET placa = ?
                                                                WHERE id = ?
                                                                """, (placa, opcao))

                                                                conn.commit()

                                                                print('Placa do veículo atualizada com sucesso!')
                                                                break
                                                        
                                                        else:
                                                                print('Digite um valor válido!')
                                                                continue
                                                
                                        
                                                except ValueError:
                                                        print('Digite um valor valido!\n')
                                                        continue                     
                
                        except ValueError:
                                print("""===============================
                                                Pessoas Cadastradas      
                                         -------------------------------""")
                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                cursor = conn.cursor()

                                cursor.execute("""
                                SELECT * FROM proprietarios;
                                """)

                                for pessoa in cursor.fetchall():
                                        dado = list(pessoa)
                                        if opcao in dado:
                                                print(f"""
                                                ===============================
                                                ID VEÍCULO: {dado[0]}
                                                NOME VEÍCULO: {dado[1]}
                                                MARCA: {dado[2]}
                                                CATEGORIA: {dado[3]}
                                                COR: {dado[4]}
                                                TIPO DE MOTOR: {dado[5]}
                                                COMBUSTÍVEL: {dado[6]}
                                                ANO: {dado[7]}
                                                Nº DE PORTAS: {dado[8]}
                                                Nº DE PASSAGEIROS: {dado[9]}
                                                PLACA: {dado[10]}
                                                DATA DE CRIAÇÃO: {dado[11]}""")
                                                conn.close()
                                                break
                                        else:
                                                print("ID DE VEÍCULO NÃO ENCONTRADO!!!"
                                                      "FAVOR DIGITE NOVAMENTE!")
                                                continue
                                continue
        
        
        def exibir_veiculos(self): #OK
                while True:
                                                
                        try:
                      
                                opcao = input("Digite o ID do Veículo desejado ou "
                                              "Pressione Enter para ver os veículos cadastrados: ")

                                print("""===============================
                                               Veículos Cadastrados      
                                         -------------------------------""")
                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                cursor = conn.cursor()

                                # cursor.execute("""
                                # SELECT * FROM veiculos;
                                # """)

                                for pessoa in cursor.fetchall():
                                        dado = list(pessoa)
                                        if opcao in dado:
                                                print(f"""
                                                ===============================
                                                ID VEÍCULO: {dado[0]}
                                                NOME VEÍCULO: {dado[1]}
                                                MARCA: {dado[2]}
                                                CATEGORIA: {dado[3]}
                                                COR: {dado[4]}
                                                TIPO DE MOTOR: {dado[5]}
                                                COMBUSTÍVEL: {dado[6]}
                                                ANO: {dado[7]}
                                                Nº DE PORTAS: {dado[8]}
                                                Nº DE PASSAGEIROS: {dado[9]}
                                                PLACA: {dado[10]}
                                                DATA DE CRIAÇÃO: {dado[11]}""")
                                                conn.close()
                                                break
                                        else:
                                                print("ID DE VEÍCULO NÃO ENCONTRADO!!!"
                                                      "FAVOR DIGITE NOVAMENTE!")
                                                continue
                                                                
                        except ValueError:
                                
                                print("""===============================
                                               Veículos Cadastrados       
                                         -------------------------------""")
                                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                                cursor = conn.cursor()

                                # cursor.execute("""
                                # SELECT * FROM proprietarios;
                                # """)

                                for pessoa in cursor.fetchall():
                                        dado = list(pessoa)
                                        print(f"""
                                               ===============================
                                               ID CLIENTE: {dado[0]}
                                               NOME: {dado[1]}
                                               CPF: {dado[2]}
                                               IDADE: {dado[3]}
                                               CRIADO EM: {dado[4]}""")
                                conn.close()
                                break
        
        
        def adicionar_coluna_veiculo(self):
                pass
        
        
        def remover_coluna_veiculo(self):
                pass


# print(f"{' Cadastrando Proprietário ':=^60}")

# Objetos de teste:

p1 = Proprietario('Davy', '106.511.439-77', 21) 
p2 = Proprietario('Arthur', '123.456.789-10', 27) 
p3 = Proprietario('Bruno', '987.654.32-100', 30) 


# v1 = Veiculo('City', 'Honda', 'Sedan', 'Prata', 'Combustão', 'Flex', 2011, 4, 5, 'MIX8904')
# v2 = Veiculo('Gol', 'VW', 'Hatch', 'Branco', 'Combustão', 'Gasolina', 2000, 4, 5, 'PLA1234')
# v3 = Veiculo('Corsa', 'GM', 'Hatch', 'Cinza', 'Combustão', 'Flex', 2005, 4, 5, 'COR4562')

# p1.salvar_proprietario()
# p2.salvar_proprietario()
# p3.salvar_proprietario()

# v1.salvar_veiculo()
# v2.salvar_veiculo()
# v3.salvar_veiculo()

p1.atualizar_proprietario()













# nome_proprietario = input("Digite o nome do Proprietario do veiculo: ")
# cpf = input("CPF do Proprietario: ")
# idade = int(input("Digite a Idade do Proprietario: "))

# nome_veiculo = input("Digite o nome do veiculo: ")
# marca = input("Digite a marca do veiculo: ")
# categoria = input("Digite a categoria do veiculo: ")
# cor = input("Digite a cor do veiculo: ")
# tipo_motor = input("Digite o tipo do motor do veiculo: ")
# combustivel = input("Digite o tipo de combustivel do veiculo: ")
# ano = int(input("Digite o Ano do veiculo: "))
# num_portas = int(input("Digite o numero de portas do veiculo: "))
# qtd_passageiros = int(input("Digite o nº de passageiros suportado pelo veiculo: "))
# placa = input("Digite a PLACA do veiculo: ")
# criado_em = input("Data de criação: ")

# obj_proprietario = Proprietario(nome_proprietario, cpf, idade)

# Veiculo(nome_veiculo, marca, categoria, 
#         cor, tipo_motor, combustivel, ano, 
#         num_portas, qtd_passageiros, placa, 
#         obj_proprietario.nome_proprietario, criado_em).salvar_veiculo_bd()
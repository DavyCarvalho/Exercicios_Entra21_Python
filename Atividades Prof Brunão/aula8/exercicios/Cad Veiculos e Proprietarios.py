import sqlite3
from time import sleep
from os import system, name

class Proprietario():
        
        def __init__(self, nome_proprietario:str, id_veiculo:int, cpf:str, idade:int):
                self.nome_proprietario = nome_proprietario
                self.id_veiculo = id_veiculo
                self.cpf = cpf
                self.idade = idade
        
        
        def salvar_proprietario(self):
                conn = sqlite3.connect('proprietarios_e_veiculos.d')
                cursor = conn.cursor()
                
                tupla_dados_proprietario = (self.nome_proprietario, self.id_veiculo, 
                                            self.cpf, self.idade)
                
                cursor.execute("""
                               INSERT INTO proprietarios 
                               (nome_proprietario, id_veiculo, cpf, idade)
                               VALUES (?,?,?,?)
                               """, tupla_dados_proprietario)
                conn.commit()
                conn.close()
                
                print(f"{' Proprietário Cadastrado com sucesso! ':'*'^50}")
                

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
                        
        
        def atualizar_proprietario(self):
                pass
        
        
        def exibir_proprietario(self):
                
                while True:
                        opcao = input("Digite o ID do cliente desejado ou Pressione Enter para ver os clientes cadastrados: ")
                        
                        try:
                                                               
                                if opcao == "":
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
                                                        ID PESSOA: {dado[0]}
                                                        NOME: {dado[1]}
                                                        ID VEÍCULO: {dado[2]}
                                                        CPF: {dado[3]}
                                                        IDADE: {dado[4]}
                                                        CRIADO EM: {dado[5]}""")
                                        conn.close()
                                        break
                                        
                                elif opcao == int:
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
                                                        ID PESSOA: {dado[0]}
                                                        NOME: {dado[1]}
                                                        ID VEÍCULO: {dado[2]}
                                                        CPF: {dado[3]}
                                                        IDADE: {dado[4]}
                                                        CRIADO EM: {dado[5]}""")
                                                        conn.close()
                                                else:
                                                        print("ID NÃO ENCONTRADO! FAVOR DIGITE NOVAMENTE!")
                                                        continue
                                        break
                        #ValueError                                        
                        except opcao != int and opcao != "":
                                print("Valor invalido! Digite um Número de ID!")
                                continue  
        
        
        def adicionar_coluna_proprietario(self):
                pass
        
        
        def remover_coluna_proprietario(self):
                pass
        
        
        
class Veiculo():

        def __init__(self, nome_veiculo:str, marca:str, modelo_categoria:str,
                           cor:str, tipo_motor:str, combustivel:str, ano:int,
                           num_portas:int, qtd_passageiros:int, placa:str):
                self.nome_veiculo = nome_veiculo
                self.marca = marca
                self.modelo_categoria = modelo_categoria
                self.cor = cor
                self.tipo_motor = tipo_motor
                self.combustivel = combustivel
                self.ano = ano
                self.num_portas = num_portas
                self.qtd_passageiros = qtd_passageiros
                self.placa = placa
        
        
        def salvar_veiculo(self):
                conn = sqlite3.connect('proprietarios_e_veiculos.db')
                cursor = conn.cursor()


                tupla_dados_veiculo = (self.nome_veiculo, self.marca, self.modelo_categoria, 
                self.cor, self.tipo_motor, self.combustivel, self.ano, 
                self.num_portas, self.qtd_passageiros, self.placa)
                

                cursor.execute("""
                                INSERT INTO veiculos (nome_veiculo, marca, modelo_categoria, 
                                cor, tipo_motor, combustivel, ano, 
                                num_portas, qtd_passageiros, placa)
                                VALUES (?,?,?,?,?,?,?,?,?,?)
                                """, tupla_dados_veiculo)
                conn.commit()
                conn.close()

                print(f"{'Veículo cadastrado com sucesso':'*'^50}")


        def excluir_veiculo(self):
                pass
        
        
        def atualizar_veiculo(self):
                pass
        
        
        def exibir_veiculos(self):
                pass
        
        
        def adicionar_coluna_veiculo(self):
                pass
        
        
        def remover_coluna_veiculo(self):
                pass


"""
Objetos de teste:

Proprietario('Davy', 1, '106.511.439-77', 21)
Veiculo('City', 'Honda', 'Sedan', 'Prata', 'Combustão', 'Flex', 2011, 4, 5, 'MIX8904')

"""

print(f"{' Cadastrando Proprietário ':=^60}")


















# nome_proprietario = input("Digite o nome do Proprietario do veiculo: ")
# cpf = input("CPF do Proprietario: ")
# idade = int(input("Digite a Idade do Proprietario: "))

# nome_veiculo = input("Digite o nome do veiculo: ")
# marca = input("Digite a marca do veiculo: ")
# modelo_categoria = input("Digite a categoria do veiculo: ")
# cor = input("Digite a cor do veiculo: ")
# tipo_motor = input("Digite o tipo do motor do veiculo: ")
# combustivel = input("Digite o tipo de combustivel do veiculo: ")
# ano = int(input("Digite o Ano do veiculo: "))
# num_portas = int(input("Digite o numero de portas do veiculo: "))
# qtd_passageiros = int(input("Digite o nº de passageiros suportado pelo veiculo: "))
# placa = input("Digite a PLACA do veiculo: ")
# criado_em = input("Data de criação: ")

# obj_proprietario = Proprietario(nome_proprietario, cpf, idade)

# Veiculo(nome_veiculo, marca, modelo_categoria, 
#         cor, tipo_motor, combustivel, ano, 
#         num_portas, qtd_passageiros, placa, 
#         obj_proprietario.nome_proprietario, criado_em).salvar_veiculo_bd()
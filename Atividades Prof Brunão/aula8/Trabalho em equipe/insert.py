import sqlite3


class Pessoa():
    
    def __init__(self, nome: str, data_nascimento: str, cpf: str,
                 endereco: str, salario: float, profissao: str,
                 email: str, telefone: str, nome_de_responsavel: str,
                 sexo: str, naturalidade: str, nacionalidade: str):

        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco
        self.salario = salario
        self.profissao = profissao
        self.email = email
        self.telefone = telefone
        self.nome_de_responsavel = nome_de_responsavel
        self.sexo = sexo
        self.naturalidade = naturalidade
        self.nacionalidade = nacionalidade


    def salvar_pessoa_na_tabela(self):

        conn = sqlite3.connect(
            'cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()

        tupla_dados_pessoa = (self.nome, self.data_nascimento,
                              self.cpf, self.endereco, self.salario,
                              self.profissao, self.email, self.telefone,
                              self.nome_de_responsavel, self.sexo,
                              self.naturalidade, self.nacionalidade)

        cursor.execute("""
                        INSERT INTO cadastro_de_pessoas (nome, data_nascimento, 
                                                        cpf, endereco, salario, profissao, email,
                                                        telefone, nome_de_responsavel, sexo, 
                                                        naturalidade, nacionalidade) 
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?)""", tupla_dados_pessoa)

        print('Pessoa cadastrada com sucesso!!! ')
        conn.commit()
        conn.close()


    def delete_pessoa(self):
        
        id_cliente =input("Digite o ID da pessoa que você deseja excluir do cadastro!\n")
        
        conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM cadastro_de_pessoas
        WHERE id_pessoa = ?
        """, (id_cliente,))
        
        print('Cliente APAGADO!\n')
        
        conn.commit()
        conn.close()


    def update_pessoa(self):
                
        while True:
            
            try:
                opcao = int(input("Digite o ID do cliente que deseja atualizar ou "
                                    "Tecle Enter para vizualizar todos os clientes!\n"))
                
                conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
                cursor = conn.cursor()

                cursor.execute("""
                SELECT * FROM cadastro_de_pessoas;
                """)
                
                verificador = False

                for pessoa in cursor.fetchall():
                        if opcao in pessoa:
                                
                                verificador = True
                                
                                print(f"===============================\n"
                                f"ID CLIENTE: {pessoa[0]} - BLOQUEADO CONTRA ALTERAÇÕES\n"
                                f"NOME: {pessoa[1]}\n"
                                f"DATA DE NASCIMENTO: {pessoa[2]}\n"
                                f"CPF: {pessoa[3]}\n"
                                f"ENDEREÇO: {pessoa[4]}\n"
                                f"SALÁRIO: {pessoa[5]}\n" 
                                f"PROFISSÃO: {pessoa[6]}\n" 
                                f"EMAIL: {pessoa[7]}\n" 
                                f"TELEFONE: {pessoa[8]}\n" 
                                f"NOME DE RESPONSÁVEL: {pessoa[9]}\n" 
                                f"SEXO: {pessoa[10]}\n"
                                f"NATURALIDADE: {pessoa[11]}\n"
                                f"NACIONALIDADE: {pessoa[12]}\n")
                                conn.close()
                                break
                        
                if not verificador:
                        print("ID DE CLIENTE NÃO ENCONTRADO!!!"
                        "FAVOR DIGITE NOVAMENTE!\n")
                        continue

                        
                print("Opções de colunas:\n\n"
                        
                            "1)NOME\n"
                            "2)DATA DE NASCIMENTO\n"
                            "3)CPF\n"
                            "4)ENDEREÇO\n"
                            "5)SALÁRIO\n"
                            "6)PROFISSÃO\n"
                            "7)EMAIL\n"
                            "8)TELEFONE\n"
                            "9)NOME DE RESPONSÁVEL\n"
                            "10)SEXO\n"
                            "11)NATURALIDADE\n"
                            "12)NACIONALIDADE\n")
                
                while True:
                        
                        verificador=True
                        
                        try:
                                coluna_alterar_tabela = int(input("Digite o Nº da opção que você deseja alterar na tabela PESSOAS?\n"))
                                
                                conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
                                cursor = conn.cursor()
                                
                                dados_tabela_proprietarios = cursor.execute("""PRAGMA table_info(cadastro_de_pessoas)""")
                                                                                
                                for tuplas in dados_tabela_proprietarios:
                                        if coluna_alterar_tabela == 0:
                                            
                                            print('Valor invalido! Digite novamente!\n')
                                            
                                            break                                                         

                                        elif tuplas[0] == coluna_alterar_tabela:
                                            
                                            alteracao = input("Digite a nova informação!\n")

                                            cursor.execute(f"""
                                            UPDATE cadastro_de_pessoas
                                            SET '{tuplas[1]}' = '{alteracao}'
                                            WHERE id_pessoa = '{tuplas[0]}'
                                            """)

                                            conn.commit()
                                            
                                            print('Atualização realizada com sucesso!')
                                            
                                            conn.close()

                                            
                                            verificador = False
                                            break
                                                        
                        except ValueError:
                            print('Digite um valor valido!\n')
                            continue #Desnecessário pois ele vai continuar o while true de qlquer maneira!!!!
                        
                        if not verificador:
                            break
                                                
    
            except ValueError:
                print("===============================\n"
                            "      Pessoas Cadastradas\n"    
                      "-------------------------------\n")
                conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
                cursor = conn.cursor()

                cursor.execute("""
                SELECT * FROM cadastro_de_pessoas;
                """)

                for pessoa in cursor.fetchall():
                        print(f"===============================\n"
                                f"ID CLIENTE: {pessoa[0]} - BLOQUEADO CONTRA ALTERAÇÕES\n"
                                f"NOME: {pessoa[1]}\n"
                                f"DATA DE NASCIMENTO: {pessoa[2]}\n"
                                f"CPF: {pessoa[3]}\n"
                                f"ENDEREÇO: {pessoa[4]}\n"
                                f"SALÁRIO: {pessoa[5]}\n" 
                                f"PROFISSÃO: {pessoa[6]}\n" 
                                f"EMAIL: {pessoa[7]}\n" 
                                f"TELEFONE: {pessoa[8]}\n" 
                                f"NOME DE RESPONSÁVEL: {pessoa[9]}\n" 
                                f"SEXO: {pessoa[10]}\n"
                                f"NATURALIDADE: {pessoa[11]}\n"
                                f"NACIONALIDADE: {pessoa[12]}\n")
                conn.close()
                continue
            
            if not verificador:
                            break


    def exibir_pessoa(self):
        
        option =input("Digite o ID da pessoa que você deseja vizualizar o cadastro: \n")
        conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM cadastro_de_pessoas
            WHERE id_pessoa = ?
        """, (option,))
        
        for linha in cursor.fetchall():
            print(f"""
        ID: {linha[0]}
        NOME: ​​​​​​​{linha[1]}
        DATA DE NASCIMENTO: {linha[2]}​​​​​​​
        CPF: {linha[3]}​​​​​​​
        ENDEREÇO: {linha[4]}​​​​​​​
        SALÁRIO: {linha[5]}​​​​​​​
        PROFISSÃO: {linha[6]}​​​​​​​
        E-MAIL: {linha[7]}​​​​​​​
        TELEFONE: {linha[8]}​​​​​​​
        NOME DO RESPONSÁVEL: {linha[9]}​​​​​​​
        SEXO: {linha[10]}​​​​​​​
        NATURALIDADE: {linha[11]}​​​​​​​
        NACIONALIDADE: {linha[12]}​​​​​​​
        """)


class Carro():
    
    def __init__(self, nome_veiculo: str, marca: str, modelo_categoria: str,
                 cor: str, tipo_motor: str, combustivel: str, ano: int,
                 num_portas: int, qtd_passageiros: int, placa: str,
                 criado_em: str):

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
        self.criado_em = criado_em


    def salvar_veiculo_na_tabela(self):
        conn = sqlite3.connect(
            'cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()

        tupla_dados_veiculo = (self.nome_veiculo, self.marca, self.modelo_categoria,
                               self.cor, self.tipo_motor,
                               self.combustivel, self.ano, self.num_portas,
                               self.qtd_passageiros, self.placa,
                               self.criado_em)

        cursor.execute("""
                        INSERT INTO cadastro_de_veiculos (nome_veiculo, marca, 
                        modelo_categoria, cor, tipo_motor, combustivel, ano,
                        num_portas, qtd_passageiros, placa, criado_em)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?)""", tupla_dados_veiculo)

        conn.commit()
        conn.close()
        
        print("Veículo Salvo com sucesso!!!")


    def delete_veiculo(self):
        
        id_veiculo =input("Digite o ID do veículo que você deseja excluir do cadastro!\n")
        
        conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()

        cursor.execute("""
        DELETE FROM cadastro_de_veiculos
        WHERE id_veiculo = ?
        """, (id_veiculo,))
        
        print('Veículo APAGADO com sucesso!')
        
        conn.commit()
        conn.close()


    def update_veiculo(self):
        while True:
            
            try:
                opcao = int(input("Digite o ID do veículo que deseja atualizar ou "
                                    "Tecle Enter para vizualizar todos os veículos!\n"))
                
                conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
                cursor = conn.cursor()

                cursor.execute("""
                SELECT * FROM cadastro_de_veiculos;
                """)
                
                verificador = False

                for pessoa in cursor.fetchall():
                        if opcao in pessoa:
                                
                                verificador = True
                                
                                print(f"===============================\n"
                                f"ID VEÍCULO: {pessoa[0]} - BLOQUEADO CONTRA ALTERAÇÕES\n"
                                f"NOME DO VEÍCULO: {pessoa[1]}\n"
                                f"MARCA: {pessoa[2]}\n"
                                f"MODELO/CATEGORIA: {pessoa[3]}\n"
                                f"COR: {pessoa[4]}\n"
                                f"TIPO DE MOTOR: {pessoa[5]}\n" 
                                f"COMBUSTÍVEL: {pessoa[6]}\n" 
                                f"ANO: {pessoa[7]}\n" 
                                f"NÚMERO DE PORTAS: {pessoa[8]}\n" 
                                f"QUANTIDADE DE PASSAGEIROS: {pessoa[9]}\n" 
                                f"PLACA: {pessoa[10]}\n"
                                f"CRIADO EM: {pessoa[11]} - BLOQUEADO CONTRA ALTERAÇÕES\n")
                                conn.close()
                                break
                        
                if not verificador:
                        print("ID DE CLIENTE NÃO ENCONTRADO!!!"
                        "FAVOR DIGITE NOVAMENTE!\n")
                        continue

                        
                print("Opções de colunas:\n\n"
                        
                            "1)NOME DO VEÍCULO:\n"
                            "2)MARCA:\n"
                            "3)MODELO/CATEGORIA:\n"
                            "4)COR\n"
                            "5)TIPO DE MOTOR\n"
                            "6)COMBUSTÍVEL\n"
                            "7)ANO\n"
                            "8)NÚMERO DE PORTAS\n"
                            "9)NOME DE RESPONSÁVEL\n"
                            "10)QUANTIDADE DE PASSAGEIROS\n"
                            "11)PLACA\n")
                
                while True:
                        
                        verificador=True
                        
                        try:
                                coluna_alterar_tabela = int(input("Digite o Nº da opção que você deseja alterar na tabela VEICULOS?\n"))
                                
                                conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
                                cursor = conn.cursor()
                                
                                dados_tabela_proprietarios = cursor.execute("""PRAGMA table_info(cadastro_de_veiculos)""")
                                                                                
                                for tuplas in dados_tabela_proprietarios:
                                        if coluna_alterar_tabela == 0:
                                            
                                            print('Valor invalido! Digite novamente!\n')
                                            
                                            break                                                         

                                        elif tuplas[0] == coluna_alterar_tabela:
                                            
                                            alteracao = input("Digite a nova informação!\n")

                                            cursor.execute(f"""
                                            UPDATE cadastro_de_veiculos
                                            SET '{tuplas[1]}' = '{alteracao}'
                                            WHERE id_veiculo = '{tuplas[0]}'
                                            """)

                                            conn.commit()
                                            
                                            print('Atualização realizada com sucesso!\n')
                                            
                                            conn.close()

                                            
                                            verificador = False
                                            break
                                                        
                        except ValueError:
                            print('Digite um valor valido!\n')
                            continue #Desnecessário pois ele vai continuar o while true de qlquer maneira!!!!
                        
                        if not verificador:
                            break
                                                
    
            except ValueError:
                print("===============================\n"
                            "      Veículos Cadastrados\n"    
                      "-------------------------------\n")
                conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
                cursor = conn.cursor()

                cursor.execute("""
                SELECT * FROM cadastro_de_veiculos;
                """)

                for pessoa in cursor.fetchall():
                        print(f"===============================\n"
                                f"ID VEÍCULO: {pessoa[0]} - BLOQUEADO CONTRA ALTERAÇÕES\n"
                                f"NOME DO VEÍCULO: {pessoa[1]}\n"
                                f"MARCA: {pessoa[2]}\n"
                                f"MODELO/CATEGORIA: {pessoa[3]}\n"
                                f"COR: {pessoa[4]}\n"
                                f"TIPO DE MOTOR: {pessoa[5]}\n" 
                                f"COMBUSTÍVEL: {pessoa[6]}\n" 
                                f"ANO: {pessoa[7]}\n" 
                                f"NÚMERO DE PORTAS: {pessoa[8]}\n" 
                                f"QUANTIDADE DE PASSAGEIROS: {pessoa[9]}\n" 
                                f"PLACA: {pessoa[10]}\n"
                                f"CRIADO EM: {pessoa[11]} - BLOQUEADO CONTRA ALTERAÇÕES\n")
                conn.close()
                continue
            
            if not verificador:
                            break


    def exibir_veiculo(self):
        option =input("Digite o ID do veículo que você deseja vizualizar o cadastro: \n")
        conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM cadastro_de_veiculos
            WHERE id_veiculo = ?
        """, (option,))
        
        for linha in cursor.fetchall():
            print(f"""
                  ID VEÍCULO: {linha[0]} 
                  NOME DO VEÍCULO: {linha[1]}
                  MARCA: {linha[2]}
                  MODELO/CATEGORIA: {linha[3]}
                  COR: {linha[4]}
                  TIPO DE MOTOR: {linha[5]}
                  COMBUSTÍVEL: {linha[6]}
                  ANO: {linha[7]}
                  NÚMERO DE PORTAS: {linha[8]}
                  QUANTIDADE DE PASSAGEIROS: {linha[9]}
                  PLACA: {linha[10]}
                  CRIADO EM: {linha[11]}
                  """)



davy = Pessoa('Davy','11/01/99','10651143977', 'R itajai', 1000.0, 'Programador', 'davy@davy', '9999', 'Marcia', 'M', 'BNU', 'BR')
carru = Carro('GOL', 'VW', 'HATCH', 'BRANCA','FLEX', 'GASOLINA', 2000, 4, 5, 'MIX8904', '22/11/2020')

# davy.salvar_pessoa_na_tabela()

# davy.update_pessoa()

# davy.delete_pessoa()

# davy.exibir_pessoa()

# carru.salvar_veiculo_na_tabela()

# carru.update_veiculo()

# carru.delete_veiculo()

# carru.exibir_veiculo()

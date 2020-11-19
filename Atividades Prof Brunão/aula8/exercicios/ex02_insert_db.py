import sqlite3
from time import sleep

class Proprietario():
        def __init__(self, nome_proprietario:str, cpf:str, idade:int):
                self.nome_proprietario = nome_proprietario
                self.cpf = cpf
                self.idade = idade

class Veiculo():

        def __init__(self, nome_veiculo:str, marca:str, modelo_categoria:str,
                           cor:str, tipo_motor:str, combustivel:str, ano:int,
                           num_portas:int, qtd_passageiros:int, placa:str,
                           nome_proprietario:object, criado_em:str):
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
                self.nome_proprietario = nome_proprietario
                self.criado_em = criado_em
        
        
        def salvar_veiculo_bd(self):
                conn = sqlite3.connect('veiculos.db')
                cursor = conn.cursor()


                tupla_dados_veiculo = (self.nome_veiculo, self.marca, self.modelo_categoria, 
                self.cor, self.tipo_motor, self.combustivel, self.ano, 
                self.num_portas, self.qtd_passageiros, self.placa, 
                self.nome_proprietario, self.criado_em)
                

                cursor.execute(f"""
                                INSERT INTO veiculos (nome_veiculo, marca, modelo_categoria, 
                                cor, tipo_motor, combustivel, ano, 
                                num_portas, qtd_passageiros, placa, 
                                nome_proprietario, criado_em)
                                VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
                                """, tupla_dados_veiculo)
                conn.commit()

                conn.close()

                return print("Veículo cadastrado com sucesso")

print(f"{'Cadastrando Proprietário':=^50}")

nome_proprietario = input("Digite o nome do Proprietario do veiculo: ")
cpf = input("CPF do Proprietario: ")
idade = int(input("Digite a Idade do Proprietario: "))

nome_veiculo = input("Digite o nome do veiculo: ")
marca = input("Digite a marca do veiculo: ")
modelo_categoria = input("Digite a categoria do veiculo: ")
cor = input("Digite a cor do veiculo: ")
tipo_motor = input("Digite o tipo do motor do veiculo: ")
combustivel = input("Digite o tipo de combustivel do veiculo: ")
ano = int(input("Digite o Ano do veiculo: "))
num_portas = int(input("Digite o numero de portas do veiculo: "))
qtd_passageiros = int(input("Digite o nº de passageiros suportado pelo veiculo: "))
placa = input("Digite a PLACA do veiculo: ")
criado_em = input("Data de criação: ")

obj_proprietario = Proprietario(nome_proprietario, cpf, idade)

Veiculo(nome_veiculo, marca, modelo_categoria, 
        cor, tipo_motor, combustivel, ano, 
        num_portas, qtd_passageiros, placa, 
        obj_proprietario.nome_proprietario, criado_em).salvar_veiculo_bd()
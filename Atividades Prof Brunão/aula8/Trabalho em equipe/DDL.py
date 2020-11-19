import sqlite3

class Pessoa():
    def __init__(self, nome:str, data_nascimento:str, cpf:str, 
                 endereco:str, salario:float, profissao:str,
                 email:str, telefone:str, nome_de_responsavel:str,
                 sexo:str, naturalidade:str, nacionalidade:str):
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
        
        conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
        cursor = conn.cursor()
        
        tupla_dados_veiculo = (self.nome, self.data_nascimento, 
                               self.cpf, self.endereco, self.salario,
                               self.profissao, self.email,self.telefone,
                               self.nome_de_responsavel, self.sexo,
                               self.naturalidade, self.nacionalidade)
        
        cursor.execute("""
                        INSERT INTO cadastro_de_pessoas (id_veiculo_pessoa, nome, data_nascimento, 
                                                        cpf, endereco, salario, profissao, email,
                                                        telefone, nome_de_responsavel, sexo, 
                                                        naturalidade, nacionalidade) 
                        VALUES (?,?,?,?,?,?,?,?,?,?,?)""", tupla_dados_veiculo)
        
class Carro():
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
    
    def salvar_veiculo_na_tabela(self):
        pass
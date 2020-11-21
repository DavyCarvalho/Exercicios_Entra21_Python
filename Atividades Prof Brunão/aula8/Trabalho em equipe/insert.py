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


    def salvar_pessoa_na_tabela(self):# Deve retornar uma mensagem de confirmação se a ação foi executada com sucesso!

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

        conn.commit()
        conn.close()


    def delete_pessoa(self):#FELIPE
        pass


    def update_pessoa(self):#DAVY
        pass


    def exibir_pessoa(self):#FELIPE
        pass


    def inserir_coluna_tabela_pessoa(self):#RAUL
        pass


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


    def salvar_veiculo_na_tabela(self): # Deve retornar uma mensagem de confirmação se a ação foi executada com sucesso!
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


    def delete_veiculo(self): #FELIPE
        pass


    def update_veiculo(self):#DAVY
        pass


    def exibir_veiculo(self):#FELIPE
        pass
    

    def inserir_coluna_tabela_veiculo(self):#RAUL
        pass      




#Exemplo de USO FUNCIONAL DO 'INNER JOIN' ABAIXO!

option =input("")
conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
cursor = conn.cursor()

cursor.execute("""
    SELECT cadastro_de_pessoas.nome, cadastro_de_pessoas.cpf, cadastro_de_pessoas.telefone, cadastro_de_veiculos.placa, cadastro_de_veiculos.ano, cadastro_de_veiculos.modelo_categoria, cadastro_de_veiculos.id_veiculo FROM cadastro_de_pessoas
    INNER JOIN pessoa_veiculo ON pessoa_veiculo.id_proprietario = cadastro_de_pessoas.id_pessoa
    INNER JOIN cadastro_de_veiculos ON pessoa_veiculo.id_veiculo_prop = cadastro_de_veiculos.id_veiculo
    WHERE cadastro_de_pessoas.id_pessoa = ?
""", option)


for linha in cursor.fetchall():
    dados = list(linha)
    print(f"""
NOME: {dados[0]}
CPF: {dados[1]}
TELEFONE: {dados[2]}
PLACA: {dados[3]}
ANO: {dados[4]}
MODELO: {dados[5]}
""")
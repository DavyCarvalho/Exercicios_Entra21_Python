import sqlite3

conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')

cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE cadastro_de_veiculos (
               id_veiculo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               nome_veiculo TEXT NOT NULL,
               marca TEXT NOT NULL,
               modelo_categoria TEXT NOT NULL,
               cor TEXT NOT NULL,
               tipo_motor TEXT NOT NULL,
               combustivel TEXT NOT NULL,
               ano INTEGER NOT NULL,
               num_portas INTEGER NOT NULL,
               qtd_passageiros INTEGER NOT NULL,
               placa TEXT NOT NULL,
               nome_proprietario TEXT NOT NULL,
               criado_em DATE NOT NULL
               
               );              
               """)

cursor.execute("""
               CREATE TABLE cadastro_de_pessoas (
               id_pessoa INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               id_veiculo_pessoa INTEGER NOT NULL,
               nome TEXT NOT NULL,
               data_nascimento TEXT NOT NULL,
               cpf VARCHAR(11),
               endereco TEXT NOT NULL,
               salario REAL NOT NULL,
               profissao TEXT NOT NULL,
               email TEXT NOT NULL,
               telefone VARCHAR(10) NOT NULL,
               nome_de_responsavel TEXT NOT NULL,
               sexo TEXT NOT NULL,
               naturalidade TEXT NOT NULL,
               nacionalidade TEXT NOT NULL,
               
               FOREIGN KEY (id_veiculo_pessoa) REFERENCES cadastro_de_veiculos(id_veiculo)
               );
               """)


conn.close()
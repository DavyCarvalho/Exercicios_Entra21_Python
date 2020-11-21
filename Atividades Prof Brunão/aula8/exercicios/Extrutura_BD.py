import sqlite3

conn = sqlite3.connect('proprietarios_e_veiculos.db')
cursor = conn.cursor()

cursor.executescript("""
CREATE TABLE veiculos (
        id_veiculo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_veiculo TEXT NOT NULL,
        marca TEXT NOT NULL,
        categoria TEXT NOT NULL,
        cor TEXT NOT NULL,
        tipo_motor TEXT NOT NULL,
        combustivel TEXT NOT NULL,
        ano INTEGER NOT NULL,
        num_portas INTEGER NOT NULL,
        qtd_passageiros INTEGER NOT NULL,
        placa TEXT NOT NULL,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE proprietarios (
        id_proprietario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_proprietario TEXT NOT NULL,
        cpf TEXT NOT NULL,
        idade TEXT NOT NULL,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE pessoa_veiculo (
        id_proprietario  INTEGER NOT NULL,
        id_veiculo_prop  INTEGER NOT NULL,
        FOREIGN KEY (id_proprietario) REFERENCES proprietarios(id_proprietário),
        FOREIGN KEY (id_veiculo_prop) REFERENCES veiculos(id_veiculo)
); 
""")

print('Tabela criada com sucesso.')
conn.close()

#Exemplo de USO FUNCIONAL DO 'INNER JOIN' ABAIXO!

# option =input("")
# conn = sqlite3.connect('cadastro_de_veiculos_concessionaria_do_vale.db')
# cursor = conn.cursor()

# cursor.execute("""
#     SELECT cadastro_de_pessoas.nome, cadastro_de_pessoas.cpf, cadastro_de_pessoas.telefone, cadastro_de_veiculos.placa, cadastro_de_veiculos.ano, cadastro_de_veiculos.modelo_categoria, cadastro_de_veiculos.id_veiculo FROM cadastro_de_pessoas
#     INNER JOIN pessoa_veiculo ON pessoa_veiculo.id_proprietario = cadastro_de_pessoas.id_pessoa
#     INNER JOIN cadastro_de_veiculos ON pessoa_veiculo.id_veiculo_prop = cadastro_de_veiculos.id_veiculo
#     WHERE cadastro_de_pessoas.id_pessoa = ?
# """, option)


# for linha in cursor.fetchall():
#     dados = list(linha)
#     print(f"""
# NOME: {dados[0]}
# CPF: {dados[1]}
# TELEFONE: {dados[2]}
# PLACA: {dados[3]}
# ANO: {dados[4]}
# MODELO: {dados[5]}
# """)
import sqlite3

conn = sqlite3.connect('proprietarios_e_veiculos.db')
cursor = conn.cursor()

cursor.execute("""
        CREATE TABLE veiculos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
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
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """)

cursor.execute("""
        CREATE TABLE proprietarios (
        id_proprietario INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome_proprietario TEXT NOT NULL,
        id_veiculo INTEGER NOT NULL,
        cpf TEXT NOT NULL,
        idade TEXT NOT NULL,
        criado_em DATETIME DEFAULT CURRENT_TIMESTAMP,
        
        FOREIGN KEY (id_veiculo) REFERENCES veiculos(id)
        );
        """)

print('Tabela criada com sucesso.')
conn.close()


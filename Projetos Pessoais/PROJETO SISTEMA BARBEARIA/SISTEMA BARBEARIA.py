import sqlite3

def criar_db():
    conn = sqlite3.connect('barbearia.db')
    cursor = conn.cursor()
    
    cursor.executescript("""
    CREATE TABLE Barbearia(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            endereço TEXT NOT NULL,
            qtd_clientes INTEGER NOT NULL,
            qtd_cortes_semana INTEGER NOT NULL,
            qtd_cortes_mes INTEGER NOT NULL,
            qtd_corte_ano INTEGER NOT NULL
            );
    CREATE TABLE Barbeiro(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
            );
    CREATE TABLE Clientes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            idade INTEGER NOT NULL,
            telefone TEXT NOT NULL
            );
            """)

class Barbearia():
    pass

class Babeiro():
    pass

class Cliente():
    pass


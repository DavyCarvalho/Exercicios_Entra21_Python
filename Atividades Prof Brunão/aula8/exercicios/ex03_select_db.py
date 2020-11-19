import sqlite3

conn = sqlite3.connect('veiculos.db')
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM veiculos;
""")

for linha in cursor.fetchall():
    print(linha)

conn.close()
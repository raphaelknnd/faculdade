import sqlite3

# conectando...
connection = sqlite3.connect("agenda.db")
# definindo um cursor
cursor = connection.cursor()

# criando a tabela
cursor.execute("""
CREATE TABLE clientes (
  id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nome TEXT NOT NULL,
  fone TEXT
);
""")

print('Tabela criada com sucesso.')
# deconectando...
connection.close()
import sqlite3

# conectando...
connection = sqlite3.connect("agenda.db")
# definindo um cursor
cursor = connection.cursor()

cursor.execute("""
  INSERT INTO clientes (nome, fone)
  VALUES ('Regis', '11-98877-0088')
""")

cursor.execute("""
  INSERT INTO clientes (nome, fone)
  VALUES ('Alana', '11-98855-1144')
""")

cursor.execute("""
  INSERT INTO clientes (nome, fone)
  VALUES ('Moises', '11-91122-3344')
""")

# gravando no db
connection.commit()

print("Dados inseridos com sucesso")

connection.close()
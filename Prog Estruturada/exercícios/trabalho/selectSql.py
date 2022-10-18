import sqlite3

# conectando...
connection = sqlite3.connect("agenda.db")
# definindo um cursor
cursor = connection.cursor()

cursor.execute("""
SELECT * FROM clientes;
""")

for linha in cursor.fetchall():
  print(linha)

connection.close
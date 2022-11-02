# Agenda de Contatos
import os
import sqlite3

def toLower(nome):
    return nome.lower()


def getConnection():
    path_name = os.path.dirname(os.path.realpath(__file__))
    #conectando
    connection = sqlite3.connect(os.path.join(path_name, 'agenda.db'))
    #definindo um cursor
    cursor = connection.cursor()
    #criando a tabela(se não existir)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             nome TEXT NOT NULL,
             fone TEXT
    );
    """)
    #retorna a conexão
    return connection

def adiciona(nome, tel):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        cursor.execute(f"""
        INSERT INTO contatos("nome", "fone")
        VALUES("{nome}", "{tel}");
        """)
        connection.commit()
        print("Contato Adicionado!")

        connection.close()
    except:
        print("Eroooou!")

def mostraContato(nome):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        contato = cursor.execute(f"""
        SELECT * FROM contatos WHERE nome = "{nome}";
        """).fetchall()
        print('\n'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]), contato)))

        connection.close()
    except:
        print('Contato não encontrado')

def mostraLista():
    connection = getConnection()
    cursor = connection.cursor()
    linhas = cursor.execute("SELECT * FROM contatos").fetchall()
    if len(linhas) == 0:
        print("LISTA VAZIA")
    else: 
        print('\n'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]), linhas))) 
    connection.close()

def apagaContato(nome):
    try:
        connection = getConnection()
        cursor = connection.cursor()
        # contatos = cursor.execute(f"""SELECT nome FROM contatos WHERE nome = '{nome}'""")

        cursor.execute(f"""DELETE FROM contatos WHERE nome IN (SELECT nome FROM contatos WHERE nome = '{nome}');
        """)
        connection.commit()
        print("contato apagado")

        connection.close()
    except:
        print('Contato não encontrado')

def apagaTodosContatos():
    connection = getConnection()
    cursor = connection.cursor()

    cursor.execute("DELETE FROM contatos")
    connection.commit()

    connection.close()


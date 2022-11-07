import os
import sqlite3


def tow_lower(nome):
    """convert params to lowercase"""
    return nome.lower()


def get_connection():
    """
        connect with database and create our table.
        it returns a connection with db
    """

    path_name = os.path.dirname(os.path.realpath(__file__))
    # conectando
    connection = sqlite3.connect(os.path.join(path_name, 'agenda.db'))
    # definindo um cursor
    cursor = connection.cursor()
    # criando a tabela(se não existir)
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contatos(
             id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
             nome TEXT NOT NULL,
             fone TEXT
    );
    """)
    # retorna a conexão
    return connection


def peform(query="", query_type="select"):
    """execute a given query"""
    try:
        result = ""
        connection = get_connection()
        cursor = connection.cursor()

        if query_type not in ("select", "modify"):
            raise ValueError("Invalid type of query")

        if query_type == 'modify':
            result = cursor.execute(query)
            connection.commit()

        if query_type == 'select':
            result = cursor.execute(query).fetchall()

            connection.close()

        return result

    except ValueError as error:
        raise error


def adiciona(nome, tel):
    """add a contact on database"""
    try:
        query = f"""
        INSERT INTO contatos("nome", "fone")
        VALUES("{nome}", "{tel}");
        """

        peform(query, "modify")

        print("Contato adicionado com sucesso")
    except ValueError as error:
        print(error)


def mostra_contato(nome):
    """show a contact by a it's name"""
    try:
        query = f"""
        SELECT * FROM contatos WHERE nome = "{nome}";
        """

        result = peform(query)
        if result:
            print('\n'.join(
                map(
                    lambda x: str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]),
                    result)
            ))

    except ValueError:
        print('Contato não encontrado')


def mostra_contatos():
    """show all the contacts on database"""
    results = peform("SELECT * FROM contatos")
    if results:
        print('\n'.join(
            map(
                lambda x: str(x[0]) + ' ' + str(x[1]) + ' ' + str(x[2]),
                results))
              )
    else:
        print("LISTA VAZIA")


def apaga_contato(nome):
    """delete a contact by its name"""
    try:
        query = f"""
            DELETE FROM contatos
            WHERE nome IN (SELECT nome FROM contatos WHERE nome = '{nome}');
        """

        peform(query, "modify")

        print("contato apagado")

    except ValueError:
        print("Erro ao apagar contato")


def apaga_todos_contatos():
    """delete all contacts on database"""
    try:
        peform("DELETE FROM contatos", 'modify')
        print("Todos os contatos foram deletados")
    except ValueError:
        print("Erro ao tentar apagar todos os contatos")

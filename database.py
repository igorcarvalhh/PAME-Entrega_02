import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r".\db\pythonsqlite.db"

    sql_create_materias_table = """ CREATE TABLE IF NOT EXISTS materias (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL
                                    ); """

    sql_create_professores_table = """CREATE TABLE IF NOT EXISTS professores (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL
                                );"""

    sql_create_turmas_table = """CREATE TABLE IF NOT EXISTS turmas (
                                        id integer PRIMARY KEY,
                                        professor_id integer NOT NULL,
                                        materia_id integer NOT NULL,
                                        num_alunos integer NOT NULL,
                                        FOREIGN KEY (professor_id) REFERENCES professores (id),
                                        FOREIGN KEY (materia_id) REFERENCES materias (id)
                                    );"""

    sql_create_alunos_table = """CREATE TABLE IF NOT EXISTS alunos (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    turma_id integer,
                                    FOREIGN KEY (turma_id) REFERENCES turmas (id)
                                );"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_materias_table)

        # create tasks table
        create_table(conn, sql_create_professores_table)

        create_table(conn, sql_create_turmas_table)

        create_table(conn, sql_create_alunos_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
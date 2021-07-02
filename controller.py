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

database = r".\db\pythonsqlite.db"
conn = create_connection(database)

def create(table,columns,values):
    sql = f"INSERT INTO {table}({columns}) VALUES({values})"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    return cur.lastrowid
    

def select_all(table):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()
    return rows

def find(table,id):
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table} WHERE id={id}")
    rows = cur.fetchall()
    return rows

def update(table,columns, values,id):
    sql = f"UPDATE {table} SET {columns} = {values} WHERE id = {id}"
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    return cur.lastrowid
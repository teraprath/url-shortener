import sqlite3 as sql
from functions import new

con = sql.connect("sql/database.db", check_same_thread=False)
cursor = con.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS urls (id VARCHAR(7), link VARCHAR)")
con.commit()

def insert(link: str):
    id = new()
    cursor.execute(f"INSERT INTO urls VALUES ('{id}', '{link}')")
    con.commit()

def delete(id: str):
    cursor.execute(f"DELETE FROM urls WHERE id LIKE '{id}'")
    con.commit()

def fetchall():
    cursor.execute("SELECT * FROM urls")
    res = cursor.fetchall()
    return res

def fetchone(id: str):
    cursor.execute(f"SELECT * FROM urls WHERE id LIKE '{id}'")
    res = cursor.fetchone()
    return res
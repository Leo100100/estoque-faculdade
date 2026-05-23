import mysql.connector
from mysql.connector import Error

def conectar():
   
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="rootsecret",
            database="estoque"
        )
        return conn
    except Error as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None


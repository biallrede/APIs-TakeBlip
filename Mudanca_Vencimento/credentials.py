import psycopg2
import pyodbc

def credenciais_banco():
    conn = psycopg2.connect(
                        host ='18.230.16.241',
                        port = '9432',
                        database='hubsoft',
                        user='erick_leitura',
                        password='73f4cc9b2667d6c44d20d1a0d612b26c5e1763c2'
                        )
    
    return conn
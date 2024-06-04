from flask import Flask
import psycopg2

app = Flask(__name__)

# Функция для подключения к базе данных PostgreSQL
def connect_to_db():
                 
       conn = psycopg2.connect(
        dbname="Autosite-base",
        user="postgres",
        password="Max75mx",
        host="localhost",
        port=5432
        )
       return conn

        
# Функция для получения данных  о продуктах избазы данных PostgreSQL
def get_products_from_db():
    conn = connect_to_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM products")
            products = cur.fetchall()
            cur.close()
            conn.close()
            return products
        except psycopg2.Error as e:
           print("Error fetching data from PostgreSQL", e)
        return []
    else: 
       return []
    
   
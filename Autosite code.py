import psycopg2
from http.server import HTTPServer, SimpleHTTPRequestHandler
from flask import Flask
import webbrowser
from app import connect_to_db

app = Flask(__name__)


def open_html_file_in_chrome(file_path):
  """
  Открывает HTML файл в Google Chrome.

  Args:
    file_path: Путь к HTML файлу.
  """
  try:
    # Получение пути к исполняемому файлу Chrome
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' 
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
    webbrowser.get('chrome').open_new_tab(f"file://{file_path}")
    print(f"Файл '{file_path}' открыт в Google Chrome.")
  except FileNotFoundError:
    print(f"Ошибка: Файл '{file_path}' не найден.")
  except Exception as e:
    print(f"Ошибка: Не удалось открыть файл в Google Chrome. {e}")

# Пример использования:
file_to_open = "test_2.html"  
open_html_file_in_chrome(file_to_open)

# Функция для установки соединения с базой данных
def connect_to_database():
    conn = psycopg2.connect(
        dbname="Название базы данных",
        user="postgres",
        password="Пароль",
        host="localhost",
        port="5432"
    )
    return conn

# Функция для получения данных  о продуктах из базы данных PostgreSQL
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
    
# Функция для выполнения SQL запросов к базе данных
def execute_query(query):
    conn = connect_to_database()
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()
    result = cur.fetchall()
    conn.close()
    return result

# Определяем IP адрес и порт сервера
server_address = ('127.0.0.5', 9000)

# Создаем экземпляр HTTP сервера с заданным IP адресом и портом
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Выводим информацию о запуске сервера
print("Starting server on http://{}:{}".format(server_address[0], server_address[1]) + " ...")

# Запускаем сервер и оставляем его работать в цикле
httpd.serve_forever()

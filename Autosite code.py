import psycopg2
from http.server import HTTPServer, BaseHTTPRequestHandler
from flask import Flask
import psycopg2

from app import connect_to_db

app = Flask(__name__)

# Функция для генерации HTML кода с заголовком, кнопками и формой для ввода
def generate_html_with_form(title):
    return f"""
    <html>
    <head>
        <title>{title}</title>
        <meta charset="utf-8">
        <style>
            body {{
                background-color: #333; /* Тёмно-серый цвет фона */
                color: #fff; /* Цвет текста */
            }}
            h1, .catalog-title {{
                background-color: white; /* Белый цвет фона для заголовка */
                color: black; /* Черный цвет текста для заголовка */
                padding: 10px;
                text-align: center; /* Выравниваем заголовок по центру */
            }}
            .catalog-title {{
                text-align: left; /* Выравниваем заголовок влево */
            }}
            a {{
                color: white; /* Белый цвет текста для кнопок */
                text-decoration: none; /* Убираем подчеркивание у ссылок */
                margin-right: 0.5cm; /* Отступ между кнопками - 0.5 см */
            }}
            .button-container {{
                text-align: center; /* Центрируем элементы внутри div по горизонтали */
            }}
            .popup {{
                display: none;
                position: fixed;
                width: 80%;
                height: 80%;
                top: 10%;
                left: 10%;
                background-color: #001f3f; /* Тёмно-синий цвет фона для всплывающего окна */
                color: white; /* Белый цвет текста во всплывающем окне */
                padding: 20px;
                z-index: 9999;
                font-size: 12pt; /* Размер шрифта 12 пунктов */
            }}
        </style>
    </head>
    <body style="text-align:center;">
        <h1 style="text-align:center;">{title}</h1>
        <div class="button-container">
            <a href="#">Главная</a>
            <a href="/catalog">Каталог</a>
            <a href="#" onclick="document.getElementById('popup').style.display='block';">О нас</a>
            <a href="#">Корзина</a>
        </div>
            </form>
        </div>
        <div class="popup" id="popup" onclick="this.style.display='none';">
            <p>Здравствуйте! Данный сайт является официальным интернет-магазином автосалона Cadia.<br>
            Наш автосалон предлагает широкий выбор автомобилей под любые ваши нужды.<br>
            Мы постарались сделать интернет-магазин наиболее удобным, чтобы вы могли найти подходящий лично вам автомобиль.</p>
        </div>
    </body>
    </html>
    """

# Функция для генерации HTML кода для страницы с товарами
def generate_catalog_page():
    return """
    <html>
    <html>
    <head>
        <title>Каталог</title>
        <meta charset="utf-8">
        <style>
            body {
                background-color: #333; /* Тёмно-серый цвет фона */
                color: white; /* Цвет текста */
            }
            .catalog-title {
                background-color: white; /* Белый цвет фона для заголовка */
                color: black; /* Черный цвет текста для заголовка */
                padding: 10px;
                text-align: left; /* Выравниваем заголовок влево */
            }
        </style>
    </head>
    <body>
        <h1 class="catalog-title">Товары</h1>
        <p>Вот что мы можем вам предложить.</p>
    </body>
</style>
</head>
<body>
    <div class="row">
        <h1>Товары в наличии</h1>
        <p>Выбранный товар</p>
<div class="col-md-4">
    <div class="product">
        <img src="Cars/car-1.png">
        <div class="product_info">
            <h3>Модель: AUDI A4</h3>
            <p>Цена: 33 178 - 44 707 USD</p>
            <a href="#Mymodal{{product[1]}}" class="click_to_button">Добавить в корзину</a>
        </div>
    </div>
</div>
<!-- Создаём модальное окно для оформления заказа! -->
<div id="Mymodal{{ product[0] }}" class="modal">
    <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title" id="orderModalLabel">Оформление заказа</h5>
            <a href="#" class="close">&times;</a>
        </div>
        <div class="modal-body">
            <form id="orderForm" action="/submit_order" method="POST">
                <input type="hidden" name="productId" value="{{ product[0] }}">
                <div class="form-group">
                    <label for="phoneNumber">Телефон</label>
                    <input type="text" class="form-control" id="phoneNumber" name="phoneNumber" required>
                </div>
                <button type="submit" class="btn btn-primary">Завершить оформление заказа</button>
            </form>
        </div>
    </div>
</div>
</div>
</body>
</html>
<html>
    """

# Функция для установки соединения с базой данных
def connect_to_database():
    conn = psycopg2.connect(
        dbname="Autosite-base",
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
# Создаем класс, унаследованный от BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Определяем метод для обработки GET запросов
    def do_GET(self):
        self.send_response(200)  # Отправляем код успешного ответа
        self.send_header('Content-type', 'text/html; charset=utf-8')  # Указываем тип контента как HTML с кодировкой UTF-8
        self.end_headers()
        
        if self.path == '/':  # Если запрошен корневой путь, отображаем основную страницу
            content = generate_html_with_form("Autosite-Cadia")
        elif self.path == '/home':  # Если запрошен путь /home, отображаем страницу "Главная"
            self.send_response(301)
            self.send_header('Location', '/')
            self.end_headers()
            return
        elif self.path == '/catalog':  # Если запрошен путь /catalog, отображаем страницу с товарами
            content = generate_catalog_page()
        else:
            self.send_error(404, "Страница не найдена")
            return
        
        self.wfile.write(content.encode('utf-8'))  # Отправляем HTML содержимое на страницу с указанием кодировки

# Определяем IP адрес и порт сервера
server_address = ('127.0.0.5', 9000)

# Создаем экземпляр HTTP сервера с заданным IP адресом и портом
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Выводим информацию о запуске сервера
print("Starting server on http://{}:{}".format(server_address[0], server_address[1]) + " ...")

# Запускаем сервер и оставляем его работать в цикле
httpd.serve_forever()

from http.server import HTTPServer, BaseHTTPRequestHandler

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
        <p>Здесь можете разместить информацию о товарах.</p>
    </body>
    </html>
    """

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



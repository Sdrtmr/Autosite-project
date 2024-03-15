from http.server import HTTPServer, BaseHTTPRequestHandler

# Функция для генерации HTML кода с заголовком в центре
def generate_html_with_centered_header(title):
    return f"""
    <html>
    <head>
        <title>{title}</title>
    </head>
    <body style="text-align:center;">
        <h1>{title}</h1>
    </body>
    </html>
    """

# Создаем класс, унаследованный от BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    # Определяем метод для обработки GET запросов
    def do_GET(self):
        self.send_response(200)  # Отправляем код успешного ответа
        self.send_header('Content-type', 'text/html')  # Указываем тип контента как HTML
        self.end_headers()
        
        # Генерируем HTML-код с заголовком в центре
        content = generate_html_with_centered_header("Autosite-Cadia")
        
        self.wfile.write(content.encode())  # Отправляем HTML содержимое на страницу

# Определяем IP адрес и порт сервера
server_address = ('127.0.0.5', 9000)

# Создаем экземпляр HTTP сервера с заданным IP адресом и портом
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Выводим информацию о запуске сервера
print("Starting server on http://{}:{}".format(server_address[0], server_address[1]) + " ...")

# Запускаем сервер и оставляем его работать в цикле
httpd.serve_forever()



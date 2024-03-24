from http.server import HTTPServer, SimpleHTTPRequestHandler
# Определяем IP адрес и порт сервера
server_address = ('127.0.0.5', 9000)

# Создаем экземпляр HTTP сервера с заданным IP адресом и портом
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# Выводим информацию о запуске сервера
print("Starting server on http://{}:{}".format(server_address[0], server_address[1]) + " ...")

# Запускаем сервер и оставляем его работать в цикле
httpd.serve_forever()



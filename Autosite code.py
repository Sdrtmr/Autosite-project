import tkinter as tk
from tkinter import simpledialog

def login():
    print("Вы выбрали вход.")

def register():
    print("Вы выбрали регистрацию.")

def open_car_catalog():
    print("Вы переходите в каталог автомобилей.")

# Создание главного окна
root = tk.Tk()
root.title("Автосалон")

# Лейбл с приветственным сообщением
label = tk.Label(root, text="Добро пожаловать!")
label.pack()

# Кнопка для регистрации
register_button = tk.Button(root, text="Зарегистрироваться", command=register)
def show_catalog_window():
    root = tk.Tk()

    label_catalog = tk.Label(root, text="Каталог автомобилей")
    label_catalog.pack()

    root.mainloop()

def show_registration_window():
    
    def submit():
        username = entry_username.get()
        password = entry_password.get()
        if username == "admin" and password == "password":
            print("Successfully logged in")
            root.destroy()
            show_catalog_window()
        else:
            label_error.config(text="Неправильный логин или пароль!")

    label_username = tk.Label(root, text="Логин:")
    label_username.pack()
    entry_username = tk.Entry(root)
    entry_username.pack()

    label_password = tk.Label(root, text="Пароль:")
    label_password.pack()
    entry_password = tk.Entry(root, show="*")
    entry_password.pack()

    button_submit = tk.Button(root, text="Войти", command=submit)
    button_submit.pack()

    label_error = tk.Label(root, text="", fg="red")
    label_error.pack()

show_registration_window()

# Кнопка для выхода
exit_button = tk.Button(root, text="Выход", command=root.destroy)
exit_button.pack()

root.mainloop()
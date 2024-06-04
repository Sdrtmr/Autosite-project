import tkinter as tk
from tkinter import messagebox
import webbrowser


def open_order_confirmation():
  """Открывает файл подтверждения заказа."""
  webbrowser.open_new_tab("success_order.html")  

def submit_order():
  """Обрабатывает отправку формы заказа."""
  email = email_entry.get()
  phone = phone_entry.get()

  # Проверка ввода (добавьте свои правила валидации)
  if not email or not phone:
    messagebox.showerror("Ошибка", "Пожалуйста, введите email и номер телефона.")
    return

  # Вывод сообщения подтверждения (добавьте свои сообщения)
  if messagebox.askyesno("Подтверждение заказа", f"Вы уверены, что хотите оформить заказ?\nEmail: {email}\nТелефон: {phone}"):
    # Отправьте заказ на сервер (если необходимо)

    # Откройте файл подтверждения
    open_order_confirmation()

    # Очистите поля ввода
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)

    # Закройте модальное окно
    root.destroy()

# Создание модального окна
root = tk.Tk()
root.title("оформление заказа")

# Создание элементов окна
email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root)
email_entry.pack()

phone_label = tk.Label(root, text="Номер телефона:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

submit_button = tk.Button(root, text="Завершить оформление заказа", command=submit_order)
submit_button.pack()

# Запуск модального окна
root.mainloop()




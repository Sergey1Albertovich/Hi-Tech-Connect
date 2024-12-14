import tkinter as tk
from tkinter import ttk


# Создаем главное окно
root = tk.Tk()
root.title("Контактная форма - Hi-Tech")
root.geometry("400x450")
root.configure(bg="#1e1e1e")

# Функция для вывода текста в консоль
def on_submit():
    print("Имя:", name_entry.get()) # Получаем значение NAME
    print("Email:", email_entry.get()) # Получаем значение EMAIL
    print("Сообщение:", message_text.get("1.0", tk.END))# Получаем значение Сообщения

# Создаем стиль
style = ttk.Style()
style.configure("TFrame", background="#2e2e2e")
style.configure("TLabel", background="#2e2e2e", foreground="#00ffcc", font=("Helvetica", 12))
style.configure("TEntry", font=("Helvetica", 12), padding=5)
style.configure("TButton", font=("Helvetica", 12), padding=10, background="#00ffcc", foreground="#1e1e1e")
style.map("TButton", background=[('active', '#00cc99')])



# Создаем фрейм
frame = ttk.Frame(root, padding="20")
frame.pack(fill=tk.BOTH, expand=True)



# Имя
name_label = ttk.Label(frame, text="Имя:")
name_label.pack(anchor=tk.W, pady=5)
name_entry = ttk.Entry(frame)
name_entry.pack(fill=tk.X)



# Email
email_label = ttk.Label(frame, text="Email:")
email_label.pack(anchor=tk.W, pady=5)
email_entry = ttk.Entry(frame)
email_entry.pack(fill=tk.X)



# Сообщение
message_label = ttk.Label(frame, text="Сообщение:")
message_label.pack(anchor=tk.W, pady=5)
message_text = tk.Text(frame, height=5, wrap=tk.WORD, bg="#3e3e3e", fg="#ffffff", insertbackground='white')
message_text.pack(fill=tk.BOTH)



# Кнопка отправки
submit_button = ttk.Button(frame, text="Отправить", command=on_submit)
submit_button.pack(pady=20)



# Запускаем главный цикл
root.mainloop()
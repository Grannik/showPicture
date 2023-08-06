#!/usr/bin/env python3

from tkinter import *
from PIL import Image, ImageTk
import sys

# Получаем имя файла из аргумента командной строки
filename = sys.argv[1]

# Создаем главное окно
root = Tk()

# Устанавливаем размеры окна
root.geometry("112x112")

# Открываем изображение
image = Image.open(filename)

# Преобразуем изображение в формат, который можно отображать в tkinter
photo = ImageTk.PhotoImage(image)

# Создаем виджет Label и отображаем в нем изображение
label = Label(root, image=photo)
label.pack()

def on_key_press(event):
    # Проверяем, была ли нажата комбинация клавиш Ctrl + Q
    if event.keysym == 'q' and event.state == 0x4:
        root.destroy()

# Привязываем обработчик события нажатия клавиши к окну
root.bind('<KeyPress>', on_key_press)

# Запускаем цикл обработки событий
root.mainloop()

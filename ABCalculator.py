# A/B Калькулятор

import tkinter as tk

# Функция закрытия программы
def do_close():
    root.destroy()

# Создание главного окна
root = tk.Tk()
root.geometry("280x300")
root.title("ABCalculator")


# добавление метки и заголовка
lbTitle = tk.Label(text = "A/B Калькулятор", font = ('Helvetica', 16, 'bold'), fg = '#0000cc')
lbTitle.place(x = 55, y = 20)

# Добавление кнопки расчитать
btnProcess = tk.Button(root, text = "Расчитать", font = ('Helvetica', 10, 'bold'))
btnProcess.place(x = 25, y = 250, width = 90, height = 30)

# Добавление кнопки закрытие программы
btnClose = tk.Button(root, text = "Закрыть", font = ('Helvetica', 10, 'bold'), command = do_close)
btnClose.place(x = 160, y = 250, width = 90, height = 30)


# Запуск цикла mainloop
root.mainloop()

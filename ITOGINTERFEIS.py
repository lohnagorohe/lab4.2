import tkinter as tk
# Ткинтер нужен для окошек

import ITOGBIBLIOTEKA as backend

# Глобальная переменная для списка
scds = None  # Пока пустой


# ФУНКЦИИ ДЛЯ ИНТЕРФЕЙСА (чтобы кнопки работали)

def obnova_ekrana():
    # Обновляет текст в поле
    output_text.delete(1.0, tk.END)  # Стираем все старое

    elements = scds.display()  # Берем данные из списка

    if elements:
        output_text.insert(tk.END, "Текущий список:\n")
        # Выводим по одному
        i = 0
        while i < len(elements):
            elem = elements[i]
            output_text.insert(tk.END, "[" + str(i) + "] -> " + elem + "\n")
            i = i + 1
        output_text.insert(tk.END, "\nВсего элементов: " + str(len(elements)))
    else:
        output_text.insert(tk.END, "Список пуст")


def pokaz_soobsheniya(msg):
    # Сообщение пользователю
    output_text.insert(tk.END, "\n>>> " + msg + "\n")
    output_text.insert(tk.END, "-" * 40 + "\n")
    output_text.see(tk.END)  # Прокрутка вниз

# ФУНКЦИЯ ДЛЯ ПЕРЕХОДА В КАЗИНО
def otkryt_kazino():
    # Эта функция закрывает текущее окно и открывает казино
    wmain.destroy()  # Закрываем это окно со списком

    # Тут мы пытаемся открыть другой файл
    # Важно: файл должен называться casino.py и лежать рядом
    try:
        import casino  # Импортируем файл с казино
        casino.zapusk()  # Запускаем функцию запуска внутри него
    except ImportError:
        print("Ошибка: файл casino.py не найден!")  # Если файла нет


def udalit_strukturu_nafig():
    # Кнопка удалить (по сути, то же самое, что создать пустой)
    global scds
    scds = backend.SraniyCiklicheskiyDvusvyazniySpisok()
    obnova_ekrana()
    pokaz_soobsheniya("Структура удалена")


def naiti_po_pozicii():
    # Поиск по индексу
    try:
        pos = int(entry.get())  # Получаем число из поля
        result = scds.naiti_po_pozicii(pos)

        if result != None:
            pokaz_soobsheniya("Элемент на позиции " + str(pos) + ": " + str(result))
        else:
            pokaz_soobsheniya("Элемент на позиции " + str(pos) + " не найден")
    except ValueError:
        pokaz_soobsheniya("Ошибка: введите число")
    finally:
        entry.delete(0, tk.END)  # Чистим поле ввода


def udalit_po_pozicii():
    # Удаление по индексу
    try:
        pos = int(entry.get())
        result = scds.udalit_po_pozicii(pos)

        if result != None:
            pokaz_soobsheniya("Удален элемент на позиции " + str(pos) + ": " + str(result))
            obnova_ekrana()
        else:
            pokaz_soobsheniya("Элемент на позиции " + str(pos) + " не найден")
    except ValueError:
        pokaz_soobsheniya("Ошибка: введите число")
    finally:
        entry.delete(0, tk.END)


def dobavit_v_nachalo():
    # Добавить в начало
    data = entry.get()

    if data:  # Проверяем, что данные не пустые
        scds.dobavit_v_nachalo(data)
        pokaz_soobsheniya("Добавлено в начало: " + data)
        obnova_ekrana()
    else:
        pokaz_soobsheniya("Ошибка: введите данные")

    entry.delete(0, tk.END)


def dobavit_v_konec():
    # Добавить в конец
    data = entry.get()

    if data:  # Проверяем, что данные не пустые
        scds.dobavit_v_konec(data)
        pokaz_soobsheniya("Добавлено в конец: " + data)
        obnova_ekrana()
    else:
        pokaz_soobsheniya("Ошибка: введите данные")

    entry.delete(0, tk.END)


# СОЗДАНИЕ ОКНА (Тут кнопки)

wmain = tk.Tk()
wmain.title("Циклический двусвязный список")
wmain.geometry('550x680+10+10')
wmain.configure(bg='#586BA4')

# Создаем сам список в памяти (из библиотеки)
scds = backend.SraniyCiklicheskiyDvusvyazniySpisok()

# Заголовок большой
lbl = tk.Label(wmain, text="ЦИКЛИЧЕСКИЙ ДВУСВЯЗНЫЙ СПИСОК",
               font=("Arial", 14), fg="#F5DD90", bg="#324376")
lbl.pack(pady=10, fill='x')

# Рамка для вывода текста
output_frame = tk.Frame(wmain, bg='#586BA4')
output_frame.pack(pady=10, fill='both', expand=True, padx=10)

output_label = tk.Label(output_frame,
                        text="Элементы списка:",
                        font=("Arial", 11),
                        fg="#F5DD90",
                        bg="#324376")
output_label.pack(pady=5, fill='x')

# Поле где будет текст
output_text = tk.Text(output_frame,
                      font=("Arial", 10),
                      bg="white",
                      fg="#324376",
                      height=10,
                      width=40,
                      wrap=tk.WORD)
output_text.pack(pady=5, fill='both', expand=True)

# Скроллбар
scrollbar = tk.Scrollbar(output_text)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_text.yview)

# Рамка для кнопок
button_frame = tk.Frame(wmain, bg='#586BA4')
button_frame.pack(pady=20)

# Кнопка 1
btn1 = tk.Button(button_frame,
                 text="Депнуть",
                 font=("Arial", 10),
                 bg="#F5DD90",
                 fg="#324376",
                 width=20,
                 height=2,
                 command=otkryt_kazino)
btn1.grid(row=0, column=0, padx=5, pady=5)

# Кнопка 2
btn2 = tk.Button(button_frame,
                 text="Удалить структуру",
                 font=("Arial", 10),
                 bg="#F5DD90",
                 fg="#324376",
                 width=20,
                 height=2,
                 command=udalit_strukturu_nafig)
btn2.grid(row=0, column=1, padx=5, pady=5)

# Кнопка 3
btn3 = tk.Button(button_frame,
                 text="Найти элемент по номеру",
                 font=("Arial", 10),
                 bg="#F5DD90",
                 fg="#324376",
                 width=20,
                 height=2,
                 command=naiti_po_pozicii)
btn3.grid(row=0, column=2, padx=5, pady=5)

# Кнопка 4
btn4 = tk.Button(button_frame,
                 text="Удалить элемент по номеру",
                 font=("Arial", 10),
                 bg="#F5DD90",
                 fg="#324376",
                 width=20,
                 height=2,
                 command=udalit_po_pozicii)
btn4.grid(row=1, column=0, padx=5, pady=5)

# Кнопка 5
btn5 = tk.Button(button_frame,
                 text="Добавить в начало",
                 font=("Arial", 10),
                 bg="#F5DD90",
                 fg="#324376",
                 width=20,
                 height=2,
                 command=dobavit_v_nachalo)
btn5.grid(row=1, column=1, padx=5, pady=5)

# Кнопка 6
btn6 = tk.Button(button_frame,
                 text="Добавить в конец",
                 font=("Arial", 10),
                 bg="#F5DD90",
                 fg="#324376",
                 width=20,
                 height=2,
                 command=dobavit_v_konec)
btn6.grid(row=1, column=2, padx=5, pady=5)

# Нижняя часть с вводом
bottom_frame = tk.Frame(wmain, bg='#586BA4')
bottom_frame.pack(side='bottom', fill='x', pady=20, padx=10)

entry_label = tk.Label(bottom_frame,
                       text="Введите данные (текст или число):",
                       font=("Arial", 11),
                       fg="#F5DD90",
                       bg="#324376")
entry_label.pack(pady=5, fill='x')

entry = tk.Entry(bottom_frame,
                 font=("Arial", 12),
                 bg="white",
                 fg="#324376")
entry.pack(pady=5, fill='x')

info_label = tk.Label(bottom_frame,
                      text="Для поиска и удаления введите номер позиции",
                      font=("Arial", 9),
                      fg="#F5DD90",
                      bg="#324376")
info_label.pack(pady=5)

# Запуск программы
wmain.mainloop()
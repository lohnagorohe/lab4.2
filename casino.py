import tkinter as tk
# КЛАССЫ ДЛЯ РАБОТЫ СО СПИСКОМ

class Node:
    # Узел двусвязного списка

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class CircularDoublyLinkedList:
    # Циклический двусвязный список

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_to_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            self.head.prev = new_node
            tail.next = new_node
            self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            new_node.next = new_node
            new_node.prev = new_node
            self.head = new_node
        else:
            tail = self.head.prev
            new_node.next = self.head
            new_node.prev = tail
            tail.next = new_node
            self.head.prev = new_node

    def delete_from_beginning(self):
        if self.is_empty():
            return None
        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            return data
        else:
            tail = self.head.prev
            data = self.head.data
            self.head = self.head.next
            self.head.prev = tail
            tail.next = self.head
            return data

    def delete_from_end(self):
        if self.is_empty():
            return None
        if self.head.next == self.head:
            data = self.head.data
            self.head = None
            return data
        else:
            tail = self.head.prev
            data = tail.data
            new_tail = tail.prev
            new_tail.next = self.head
            self.head.prev = new_tail
            return data

    def find_by_position(self, position):
        if self.is_empty() or position < 0:
            return None
        current = self.head
        count = 0
        while count < position:
            current = current.next
            count += 1
            if current == self.head:
                return None
        return current.data if current else None

    def delete_by_position(self, position):
        if self.is_empty() or position < 0:
            return None

        if self.head.next == self.head and position == 0:
            data = self.head.data
            self.head = None
            return data

        current = self.head
        count = 0
        while count < position:
            current = current.next
            count += 1
            if current == self.head:
                return None

        data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev

        if current == self.head:
            self.head = current.next

        return data

    def display(self):
        if self.is_empty():
            return []
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return elements


# ФУНКЦИИ ДЛЯ РАБОТЫ С ИНТЕРФЕЙСОМ

def update_display():
    # Обновление отображения списка в текстовом поле
    output_text.delete(1.0, tk.END)

    elements = cdll.display()

    if elements:
        output_text.insert(tk.END, "🎰 ТЕКУЩИЙ СПИСОК 🎰\n", "header")
        output_text.insert(tk.END, "════════════════════\n", "separator")

        # Чередуем цвета для элементов как фишки в казино
        for i, elem in enumerate(elements):
            if i % 2 == 0:
                output_text.insert(tk.END, f"♦ [{i}] → {elem}\n", "red_item")
            else:
                output_text.insert(tk.END, f"♠ [{i}] → {elem}\n", "black_item")

        output_text.insert(tk.END, f"\n💰 Всего элементов: {len(elements)}", "jackpot")
    else:
        output_text.insert(tk.END, "🍀 СТОЛ ПУСТ 🍀\n", "empty")
        output_text.insert(tk.END, "Сделайте вашу ставку!", "italic")


def show_message(msg):
    # Вывод информационного сообщения в стиле казино
    output_text.insert(tk.END, f"\n🎲 {msg} 🎲\n", "message")
    output_text.insert(tk.END, "────────────────\n", "separator")
    output_text.see(tk.END)


# Функции-обработчики для кнопок
def create_structure():
    # Новая игра - свежий стол
    global cdll
    cdll = CircularDoublyLinkedList()
    update_display()
    show_message("НОВАЯ ИГРА! Стол готов")


def delete_structure():
    # Сброс игры - все фишки убраны
    global cdll
    cdll = CircularDoublyLinkedList()
    update_display()
    show_message("СТОЛ ОЧИЩЕН! Начнем заново")


def find_by_position():
    # Поиск элемента - как найти нужную карту
    try:
        pos = int(entry.get())
        result = cdll.find_by_position(pos)

        if result is not None:
            show_message(f"ДЖЕКПОТ! На позиции {pos} найдено: {result}")
        else:
            show_message(f"❌ Позиция {pos} пуста как карман после казино")
    except ValueError:
        show_message("⚠️ ОШИБКА: Введите число! Не жульничайте!")
    finally:
        entry.delete(0, tk.END)


def delete_by_position():
    # Удаление элемента - карта уходит в колоду
    try:
        pos = int(entry.get())
        result = cdll.delete_by_position(pos)

        if result is not None:
            show_message(f"♠ СТАВКА СДЕЛАНА! Удален элемент {pos}: {result}")
            update_display()
        else:
            show_message(f"❌ Позиция {pos} пуста - ставка не принимается")
    except ValueError:
        show_message("⚠️ ОШИБКА: Введите корректное число!")
    finally:
        entry.delete(0, tk.END)


def add_to_beginning():
    # Добавление в начало - как первая карта в колоде
    data = entry.get()

    if data:
        cdll.add_to_beginning(data)
        show_message(f"♦ В НАЧАЛО КОЛОДЫ: {data}")
        update_display()
    else:
        show_message("⚠️ Введите данные! Пустая ставка не принимается")

    entry.delete(0, tk.END)


def add_to_end():
    # Добавление в конец - последняя карта в прикупе
    data = entry.get()

    if data:
        cdll.add_to_end(data)
        show_message(f"♣ В КОНЕЦ КОЛОДЫ: {data}")
        update_display()
    else:
        show_message("⚠️ Введите данные! Казино ждет вашу ставку")

    entry.delete(0, tk.END)


# СОЗДАНИЕ ГРАФИЧЕСКОГО ИНТЕРФЕЙСА В СТИЛЕ КАЗИНО

wmain = tk.Tk()
wmain.title("🎰 CASINO: Циклический двусвязный список 🎰")
wmain.geometry('550x750+10+10')
wmain.configure(bg='#0A3200')  # Темно-зеленый как игровой стол

# Создаем пустой список
cdll = CircularDoublyLinkedList()

# Заголовок в стиле казино
title_frame = tk.Frame(wmain, bg='#D4AF37')  # Золотой
title_frame.pack(pady=15, fill='x', padx=20)

lbl = tk.Label(title_frame,
               text="🎲 CASINO ROYALE 🎲\nЦИКЛИЧЕСКИЙ ДВУСВЯЗНЫЙ СПИСОК",
               font=("Arial Black", 16),
               fg="#8B0000",  # Темно-красный
               bg="#D4AF37")  # Золотой
lbl.pack(pady=10, padx=20)

# Добавляем блестящую полоску
shiny_line = tk.Frame(wmain, bg='#FFD700', height=3)
shiny_line.pack(fill='x', padx=30)

# Фрейм для области вывода
output_frame = tk.Frame(wmain, bg='#0A3200')
output_frame.pack(pady=15, fill='both', expand=True, padx=20)

# Заголовок области вывода с "игровыми" символами
output_label = tk.Label(output_frame,
                        text="♠ ♥ ♦ ♣  ИГРОВОЕ ПОЛЕ  ♠ ♥ ♦ ♣",
                        font=("Arial Black", 12),
                        fg="#FFD700",  # Золотой
                        bg="#8B0000")  # Темно-красный
output_label.pack(pady=5, fill='x')

# Текстовое поле с настраиваемыми тегами для разных цветов
output_text = tk.Text(output_frame,
                      font=("Courier New", 11),  # Моноширинный для ровных колонок
                      bg="#1A4300",  # Темно-зеленый
                      fg="#FFD700",  # Золотой текст
                      height=10,
                      width=50,
                      wrap=tk.WORD,
                      relief=tk.SUNKEN,
                      bd=5)
output_text.pack(pady=10, fill='both', expand=True)

# Настраиваем разные стили текста
output_text.tag_configure("header", foreground="#FFD700", font=("Arial Black", 12))
output_text.tag_configure("red_item", foreground="#FF4444", font=("Courier New", 11, "bold"))
output_text.tag_configure("black_item", foreground="#FFFFFF", font=("Courier New", 11))
output_text.tag_configure("jackpot", foreground="#FFD700", font=("Arial Black", 10))
output_text.tag_configure("empty", foreground="#FFD700", font=("Arial Black", 14))
output_text.tag_configure("message", foreground="#FFD700", font=("Arial", 10, "bold"))
output_text.tag_configure("separator", foreground="#8B0000")
output_text.tag_configure("italic", foreground="#FFD700", font=("Arial", 10, "italic"))

# Полоса прокрутки в стиле казино
scrollbar = tk.Scrollbar(output_text, bg="#D4AF37", troughcolor="#0A3200")
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
output_text.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=output_text.yview)

# Фрейм для кнопок (игровой автомат)
button_frame = tk.Frame(wmain, bg='#8B0000', bd=5, relief=tk.RAISED)
button_frame.pack(pady=15, padx=20, fill='x')

# Заголовок для кнопок - размещаем через grid, а не pack
button_label = tk.Label(button_frame,
                        text="🎰 ВАШИ ДЕЙСТВИЯ 🎰",
                        font=("Arial Black", 12),
                        fg="#FFD700",
                        bg="#8B0000")
button_label.grid(row=0, column=0, columnspan=3, pady=10)  # Используем grid!

# Конфигурация кнопок в стиле казино
buttons_config = [
    ("🎲 СОЗДАТЬ СТОЛ", create_structure),
    ("💣 ОЧИСТИТЬ СТОЛ", delete_structure),
    ("🔍 НАЙТИ ПОЗИЦИЮ", find_by_position),
    ("🗑 УДАЛИТЬ ПОЗИЦИЮ", delete_by_position),
    ("⬅ ДОБАВИТЬ В НАЧАЛО", add_to_beginning),
    ("➡ ДОБАВИТЬ В КОНЕЦ", add_to_end)
]

# Создаем кнопки в сетке 3x2 (начиная со второй строки)
row = 1  # Начинаем со второй строки (после заголовка)
col = 0
for text, command in buttons_config:
    # Чередуем цвета кнопок
    if (row + col) % 2 == 0:
        btn_color = "#D4AF37"  # Золотой
        text_color = "#8B0000"  # Красный
    else:
        btn_color = "#8B0000"  # Красный
        text_color = "#D4AF37"  # Золотой

    btn = tk.Button(button_frame,
                    text=text,
                    font=("Arial Black", 9),  # Чуть меньше шрифт
                    bg=btn_color,
                    fg=text_color,
                    width=16,
                    height=2,
                    relief=tk.RAISED,
                    bd=3,
                    activebackground="#FFD700",
                    activeforeground="#8B0000",
                    command=command)

    btn.grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 2:
        col = 0
        row += 1

# Фрейм для нижней части (прием ставок)
bottom_frame = tk.Frame(wmain, bg='#D4AF37', bd=5, relief=tk.RAISED)
bottom_frame.pack(side='bottom', fill='x', pady=15, padx=20)

# Заголовок поля ввода
entry_label = tk.Label(bottom_frame,
                       text="💰 СДЕЛАЙТЕ ВАШУ СТАВКУ 💰",
                       font=("Arial Black", 12),
                       fg="#8B0000",
                       bg="#D4AF37")
entry_label.pack(pady=5)

# Поле ввода
entry = tk.Entry(bottom_frame,
                 font=("Courier New", 14, "bold"),
                 bg="black",
                 fg="#00FF00",
                 insertbackground="#FFD700",
                 justify='center',
                 bd=5,
                 relief=tk.SUNKEN)
entry.pack(pady=10, padx=20, fill='x')

# Подсказка для игроков
info_label = tk.Label(bottom_frame,
                      text="♠ Для поиска и удаления введите номер позиции ♣\n♦ Можно вводить любой текст (числа/строки) ♥",
                      font=("Arial", 10, "italic"),
                      fg="#8B0000",
                      bg="#FFD700")
info_label.pack(pady=5)

# Добавляем мигающий текст
blinking_label = tk.Label(wmain,
                          text="♥ ♠ ♦ ♣ УДАЧНОЙ ИГРЫ! ♥ ♠ ♦ ♣",
                          font=("Arial Black", 10),
                          fg="#FFD700",
                          bg="#0A3200")
blinking_label.pack(pady=5)


# Функция для мигания текста
def blink():
    current_color = blinking_label.cget("fg")
    new_color = "#8B0000" if current_color == "#FFD700" else "#FFD700"
    blinking_label.config(fg=new_color)
    wmain.after(500, blink)


# Запускаем мигание
blink()

# Запуск главного цикла
wmain.mainloop()
from tkinter import *
from random import *

tk = Tk()  # Створення головного вікна програми
canvas = Canvas(tk, width=500, height=400)  # Створення полотна розміром 500x400 пікселів
canvas.pack()  # Відображення полотна на екрані

# Створюємо дорогу, повернуту на 90 градусів
canvas.create_rectangle(0, 100, 500, 300, fill="gray")  # Прямокутник, що представляє дорогу
canvas.create_line(0, 200, 500, 200, fill="white", dash=(15, 23))  # Середня роздільна лінія

# Додаємо фінішну лінію (праворуч)
canvas.create_line(450, 100, 450, 300, fill="yellow", width=3)  # Фінішна лінія праворуч

class Car:
    def __init__(self, canvas, x, y, color, name):  # Конструктор класу для створення автомобіля
        self.canvas = canvas  # Збереження посилання на полотно
        self.name = name  # Ім'я автомобіля (для визначення переможця)
        # Малюємо кузов автомобіля у вигляді прямокутника
        self.body = canvas.create_rectangle(x, y, x + 40, y + 20, fill=color, outline=color)
        # Малюємо два колеса у вигляді овалів, які будуть розташовані нижче кузова
        self.wheel1 = canvas.create_oval(x + 2, y + 18, x + 12, y + 28, fill="black")  # Ліве колесо
        self.wheel2 = canvas.create_oval(x + 28, y + 18, x + 38, y + 28, fill="black")  # Праве колесо
        self.x_speed = randint(2, 5)  # Випадкова швидкість для кожного автомобіля
        self.finished = False  # Прапорець для перевірки, чи перетнув автомобіль фініш

    def move(self):
        # Переміщуємо автомобіль тільки по горизонталі (вісь X)
        self.canvas.move(self.body, self.x_speed, 0)
        self.canvas.move(self.wheel1, self.x_speed, 0)
        self.canvas.move(self.wheel2, self.x_speed, 0)
        pos = self.canvas.coords(self.body)  # Отримуємо поточні координати кузова автомобіля

        # Перевірка, чи перетнув автомобіль фінішну лінію
        if pos[2] >= 450 and not self.finished:  # Якщо передня частина авто перетнула фінішну лінію
            self.finished = True  # Позначаємо, що автомобіль фінішував
            return self.name  # Повертаємо ім'я автомобіля

        return None  # Якщо автомобіль не фінішував, повертаємо None


# Створюємо два автомобілі
car1 = Car(canvas, randint(-200, 0), 120, "red", "Червона машина")  # Червоний автомобіль
car2 = Car(canvas, randint(-200, 0), 240, "blue", "Синя машина")  # Синій автомобіль

winner = None  # Змінна для зберігання переможця


# Функція для анімації автомобілів
def animate():
    global winner
    if winner is None:  # Якщо переможець ще не визначений
        result1 = car1.move()  # Рух першого автомобіля
        result2 = car2.move()  # Рух другого автомобіля

        # Перевіряємо, чи фінішував один із автомобілів
        if result1:
            winner = result1  # Червоний автомобіль фінішував першим
            canvas.create_text(250, 150, text=f"{result1} виграла!", font=("Arial", 20), fill="green")  # Виведення результату
        elif result2:
            winner = result2  # Синій автомобіль фінішував першим
            canvas.create_text(250, 150, text=f"{result2} виграла!", font=("Arial", 20), fill="green")  # Виведення результату

    tk.after(20, animate)  # Повторний виклик функції через 20 мілісекунд


animate()  # Запуск анімації
tk.mainloop()  # Запуск головного циклу програми

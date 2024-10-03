# Імортуємо лібу для малювання завдання.
import turtle

# Створюємо функцію для малювання однієї з сторін сніжинки Коха.
def koch_side(length, level):
    if level == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_side(length, level - 1)  # Перша частина
        turtle.left(60)
        koch_side(length, level - 1)  # Друга частина
        turtle.right(120)
        koch_side(length, level - 1)  # Третя частина
        turtle.left(60)
        koch_side(length, level - 1)  # Четверта частина

# Створюємо функцію яка буде малювати сніжинку Коха.
def koch_snowflake(length, level):
    for _ in range(3):  # Сніжинка складається з трьох сторін
        koch_side(length, level)
        turtle.right(120)

# Основна функція для запуску.
def main():
     # Запит рівня рекурсії у користувача.
    level = int(input("Введіть рівень рекурсії (наприклад, 4): "))

    # Налаштування черепашки.
    turtle.speed(0) # Максимальна швидкість малювання.
    turtle.penup()
    turtle.goto(-200, 100)  # Початкове положення.
    turtle.pendown()
    
    # Довжина сторони сніжинки.
    length = 400

    # Малювання сніжинки Коха.
    koch_snowflake(length, level)

    # Завершення малювання.
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

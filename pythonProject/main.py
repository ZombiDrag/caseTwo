import random
import time

#Выполняет плавный ввод текста
def text_slow(a):
    for i in a:
        print(i, end='',flush=True)
        time.sleep(0.05)
    return ''

# Основная логика приложения. Создает переменную ' n ' и в дальнейшем сравнивает
#  с веденными значениями пользователя и выдавать ответ виде текста с подсказкой и количеством попыток.
def rendom_number():

    n = random.randrange(0, 101)

    print("Добро пожаловать в игру угадай чесло!")
    i = 4
    while True:
        try:
            f = int(input(text_slow('Введи число:  -->')))
            if f == n:
                text_slow("Поздравляю! Вы выиграли!")
                time.sleep(20)
                break
            elif i == 0:
                print(f"Вы не угадали.\nОсталось попыток: {i}")
                time.sleep(20)
                break

            else:
                if f > n:

                    text_slow(f"Вы не угадали попробуйте уменьшить число.\nОсталось попыток: {i}. ")
                    i -= 1

                else:

                    text_slow(f"Вы не угадали попробуйте увеличить число.\nОсталось попыток: {i}. ")
                    i -= 1
        except ValueError:
            text_slow("Неверное значение попробуйте ввести целое число.\n")


if __name__ == "__main__":
    rendom_number()

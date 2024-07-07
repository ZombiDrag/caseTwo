import random
import time

#Выполняет плавный ввод текста
def text_slow(a):
    for i in a:
        print(i, end='',flush=True)
        time.sleep(0.07)
    return ''

# Основная логика приложения. Создает переменную ' n ' и в дальнейшем сравнивает
#  с веденными значениями пользователя и выдавать ответ виде текста с подсказкой и количеством попыток.
def rendom_number():

    n = random.randrange(0, 101)

    print("Добро пожаловать в игру угадай чесло!")
    for i in range(1, 5):
        f = int(input(text_slow('Введи число:  -->')))
        if f == n:
            text_slow("Поздравляю! Вы выиграли!")
            time.sleep(20)
            break
        elif i == 4:
            print(f"Вы не угадали.\nОсталось попыток: {4 - i}")
            time.sleep(20)
            break

        else:
            if f > n:
                text_slow(f"Вы не угадали попробуйте уменьшить число.\nОсталось попыток: {4 - i}. ")

            else:
                text_slow(f"Вы не угадали попробуйте увеличить число.\nОсталось попыток: {4 - i}. ")



if __name__ == "__main__":
    rendom_number()

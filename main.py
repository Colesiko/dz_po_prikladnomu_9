import logging
import random

# Настраиваем логгер
logging.basicConfig(filename='game.log', level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

def log_event(event):
    logging.info(event)

def game():
    # Запрашиваем у пользователя ввести N и k
    n = input("Введите максимальное число N: ")
    bukv = n.isdigit()
    if bukv == False:  # проверка на буквы
        while bukv == False:
            n = input("Введите число большее 1(цифрами): ")
            bukv = str.isnumeric(n)
    n = int(n)
    while n == 0:
        n = input("Введите число большее 1(цифрами): ")
        bukv = n.isdigit()
        if bukv == False:  # проверка на буквы
            while bukv == False:
                n = input("Введите число большее 1(цифрами): ")
                bukv = str.isnumeric(n)
        n = int(n)

    k = input("Введите количество попыток k: ")
    bukv = k.isdigit()
    if bukv == False:  # проверка на буквы
        while bukv == False:
            k = input("Введите число большее 1(цифрами): ")
            bukv = str.isnumeric(k)
    k = int(k)

    # Записываем событие в лог-файл
    log_event(f"start game. N={n}, k={k}")

    # Генерируем случайное число от 1 до N
    number = random.randint(1, n)
    log_event(f"zagadannoe chislo {number}")

    # Предлагаем пользователю отгадать число
    for i in range(k):
        guess = input("Ваш ответ: ")
        bukv = guess.isdigit()
        if bukv == False:  # проверка на буквы
            while bukv == False:
                guess = input("Введите число большее 1(цифрами): ")
                bukv = str.isnumeric(guess)
        guess = int(guess)

        log_event(f"popitka {i+1}: {guess}")
        if guess == number:
            print("Вы угадали!")
            log_event("ugadannoe chislo!")
            return
        elif guess < number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")

    print("Попытки закончились")
    log_event("popitki zakonchilis")

# Запускаем игру
game()

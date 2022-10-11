"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1, low_bound: int = 1, high_bound: int = 100) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        low_bound (int, optional): Минивальнодопустимое число для загадывания. Defaults to 1.
        high_bound (int, optional): Максимальнодопустимое число для загадывания. Defaults to 100.

    Returns:
        int: Число попыток
    """
    if (number < low_bound) or (number > high_bound):
        raise ValueError(f"Ошибка. Загаданное число не принадлежит допустимому диапазону от {low_bound} до {high_bound}.")

    count = 0
    predict_number = high_bound # Предполагаемое число. Начинаем угадывать с максимального значения, чтобы избежать зацикливания при number == high_bound

    while True:
        count += 1
        if number == predict_number:
            #print(f"Число {number} угадано за {count} попыток")
            break # Выход из цикла если угадали
        elif predict_number > number:
            high_bound = predict_number
            predict_number = high_bound - max(1, (high_bound - low_bound)//2) # Функция max необходима, чтобы избежать зацикливания при number == low_bound
        else:
            low_bound = predict_number
            predict_number = low_bound + (high_bound - low_bound)//2
 
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # Загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)

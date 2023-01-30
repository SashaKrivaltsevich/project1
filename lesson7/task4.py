from time import time
import requests
"""Сам декоратор"""
def decorator (func):
    """Обертка декоратора"""
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполения исходной функци:  {round(end-start, 2)} секунд')
        return wrapper

@decorator
def get_wp1():
    """
    Получаем ответ сервера
    200 - запрос успешно отработан
    """
    print('Выполняем расчет яндкес')
    res = requests.get('https://ya.ru')
    return res

@decorator
def get_wp():
    """
    Получаем ответ сервера
    200 - запрос успешно отработан
    """
    print('Выполняем расчет гугл')
    res = requests.get('https://google.com')
    return res

get_wp()
get_wp1()




from datetime import datetime
from time import sleep

def sleep_time() -> str:
    now_ = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    sleep(1)
    return now_

def range_number(n: int) -> list:
    lst = [sleep_time() for _ in range(n)]
    return lst

number = int(input('Введите число: '))

print(range_number(number))
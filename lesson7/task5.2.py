
def main():
    if text.isdigit():
        num1 = int(text)
        return 'Вы ввели положительное целое число:', num1
    try:
        v = int (text)
        if v < 0:
            return 'Вы Выели отрицательное число', v
    except:
        list1 = list(text)
    i = ','
    if i in list1:
        new_n_name = '.'
        list1 = [a if a != i else new_n_name for a in list1]
    try:
        db = float(''.join(list1))
        if db > 0:
            return 'Вы ввели положительное дробное число:', db
        else:
            return 'Вы ввели отрицательное дробное число:', db
    except:
        return 'Вы ввели не корректное число:', text


while True:
    text = input('Введите число: ')

    result = main()
    print(*result)


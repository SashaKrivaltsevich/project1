
"""Переводим лист с интовыми значениями в лист со строковыми значениями"""
# int_name = [4, 5, 6, 7, 8]
# numbers_str = map(str, int_name)
# print(list(numbers_str))

"""Перевод листа с интовыми в лист со строковыми через лямбду"""
int_name = [4, 5, 6, 7, 8]
numbers_str = list(map(lambda x: str(x), int_name))
print(list(numbers_str))
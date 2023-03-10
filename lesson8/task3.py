"""
Создать словарь в качестве ключа которого будет 6-ти значное число (id), а в
качестве значений кортеж состоящий из 2-х элементов - имя(str), возраст(int).
Сделать около 5-6 элементов словаря. Записать данный словарь на диск в json-файл.
"""

import json
import csv

DICT_TO_JSON = {
    '000001': ['Aleksandra', '18'],
    '000002': ['Elena', '42'],
    '000003': ['Daria', '20'],
    '000004': ['Sonya', '18'],
    '000005': ['Nastya', '19'],
    '000006': ['Tanya', '19']
}

with open('data1.json', 'w') as file_data:
    json.dump(DICT_TO_JSON, file_data)




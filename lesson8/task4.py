"""
Прочитать сохранённый json-файл и записать данные на диск в csv-файл, первой
строкой которого озоглавив каждый столбец и добавив новый столбец "телефон
"""
import json
import csv


with open('data1.json') as json_file:  # открываем json файл с помощью менеджера контекста
    data_dict = json.load(json_file)  # чтение файла и запись в переменную DICT_TO_JSON


my_dict_2 = {'000001': '+375331111111', '000002': '375332222222', '000003': '375333333333', '000004': '375334444444', '000005': '375335555555', '000006': '375336666666'}  # cоздадим словарь с телефонами

with open('data2.csv', 'w', encoding='utf-8') as csv_file:  # создадим и откроем csv файл
    file_writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=['id', 'name', 'age', 'phone'])
    file_writer.writeheader()
    for key, value in data_dict.items():
        file_writer.writerow({'id': key, 'name': value[0], 'age': value[1], 'phone': my_dict_2[key]})





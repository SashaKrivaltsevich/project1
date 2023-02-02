"""
Прочитать сохранённый json-файл и записать данные на диск в csv-файл, первой
строкой которого озоглавив каждый столбец и добавив новый столбец "телефон
"""
import json
import csv


"""первый способ, более понятный"""


with open('data1.json') as json_file:  # открываем json файл с помощью менеджера контекста
    DICT_TO_JSON = json.load(json_file)  # чтение файла и запись в переменную DICT_TO_JSON


my_dict_2 = {'000001': '+375331111111', '000002': '375332222222', '000003': '375333333333', '000004': '375334444444', '000005': '375335555555', '000006': '375336666666'}  # cоздадим словарь с телефонами

with open('data2.csv', 'w', encoding='utf-8') as csv_file:  # создадим и откроем csv файл
    file_writer = csv.DictWriter(csv_file, delimiter=',', fieldnames=['id', 'name', 'age', 'phone'])
    file_writer.writeheader()  # печать заголовка
    for key, value in DICT_TO_JSON.items():
        file_writer.writerow({'id': key, 'name': value[0], 'age': value[1], 'phone': my_dict_2[key]})
    # с помощью цикла for "пробегаем" по значениям словаря и записываем их в нужном формате в csv файл



# """Второй странный способ,скорее всего где-то на стэке нашла и переделала,( НЕ РАБОТАЕТ!!!) """
#
# with open('data1.json', 'r') as json_file:
#     DICT_TO_JSON = json.loads(json_file)
#     wr = csv.DictWriter(json_file, fieldnames=['id', 'name', 'age', 'phone'])
#     wr.writeheader()
#     for key, values in DICT_TO_JSON.items():
#         wr.writerow({'id': key, 'name': value[0], 'age': value[1], 'phone': my_dict_2[key]})
#
# try:
#     with open('data1.json', 'r') as f:
#         DICT_TO_JSON = json.loads(f.read())
#
#     output = ','.join([*DICT_TO_JSON[0]])
#     print(output)
#     for obj in DICT_TO_JSON:
#         output += f'\n{obj["000001"]},{obj["000002"]},{obj["000003"]},{obj["000004"]},{obj["000005"]},{obj["000006"]}'
#     print(output)
#     with open('output.csv', 'w') as f:
#         file_writer = csv.DictWriter(f, delimiter=',', fieldnames=['id', 'name', 'age', 'phone'])
#         file_writer.writeheader()
#         for key, value in DICT_TO_JSON.items():
#             file_writer.writerow({'id': key, 'name': value[0], 'age': value[1], 'phone': DICT_TO_JSON[key]})
#
# except Exception as ex:
#     print(f'Error: {str(ex)}')

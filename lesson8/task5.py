"""
Прочитать сохранённый csv-файл и сохранить данные в excel-файл, кроме возраста - столбец с этими данными
не нужен.
"""

import csv
import openpyxl


with open('data2.csv') as csv_file:
    file_reader = csv.reader(csv_file)
    data = list(file_reader)

wb = openpyxl.Workbook()
ws = wb.active

for coll_age in data:
    ws.append(coll_age)

ws.delete_cols(3)
wb.save('csv_to_excel.xlsx')
wb.close()

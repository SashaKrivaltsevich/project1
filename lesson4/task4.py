a = input('Введенная строка: ')
odd_num = a[0::2]
even_num = a[1::2]
print(a.strip(), end='\n\n\n')
print(odd_num, even_num, sep='     ', end='!!!')
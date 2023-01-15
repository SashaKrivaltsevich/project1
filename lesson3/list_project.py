# 1-ый список
list_ = ['1', '2', 'd', '4', '2', 'cat']
list_.append('dog')
list_.extend('FFF')
list_.insert(2, '3')
list_.pop(3)
list_.remove('2')
list_.sort()
print(list_)
# 2-ой список
list_2 = [list_2 * 2 for list_2 in 'Spisok' if list_2 != 's']
list_2.reverse()
list_2.copy()
print(list_2)
print(list_2.index('pp'))
print(list_2.count('i'))
# 3-ий список
list_3 = ['1', '2', '3', '4']
list_3.clear()
print(list_3)
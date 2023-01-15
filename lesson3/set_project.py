set_ = set('hello world')
set_.add('5')
set_.pop()
print(set_)
print(len(set_))
print('w' in set_)

set_2 = {i ** 2 for i in range(5)}
set_2.update('2')
print(set_2)

set_3 = ['1', '1', '3', '5', '45']
set_3.remove('45')

print(set(set_3))
set_3.clear()
print(set(set_3))

set_4= {1, 55, 34, 2, 12, 14, -4}
print(sorted(set_4))
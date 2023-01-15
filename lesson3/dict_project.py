# 1-ый  способ задания словаря, с помощью литерала
dict_ = {'dict': 1, 'dictionary': 2}
dict_.copy()
dict_.keys()
print(dict_)

# 2-oй способ задания словаря, с помощью функции dict:
dict_21 = dict(short='dict', long='dictionary')
dict_22 = dict([(1, 3), (2, 4)])

print(dict_21)
print(dict_22)

# 3-ий способ задания словаря, с помощью метода fromkeys:
dict_3= dict.fromkeys(['dict', 'dictionary'])
dict_3.clear()
print(dict_3)

# 4-ый способ задания словаря, с помощью генераторов словарей
dict_4 = {a: a ** 3 for a in range(3)}
dict_4[3] = 3 ** 3
print(dict_4)

for k, v in dict_4.items():
    print(k, v)


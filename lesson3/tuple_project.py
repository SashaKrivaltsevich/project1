tuple_ = (1, 3, 3, 5, 67)
#print(tuple.append(56))
print(tuple_.count(3))
print(tuple_.index(5))
print(tuple_.__sizeof__())

tuple_2 = tuple('hello, world!')
print(len(tuple_2))
print(max(tuple_2))
print(id(tuple_[0]) == id(tuple_2[2]))
print(id(tuple[0]), id(tuple[2]))

list_ = list(tuple_)
list_.append(2)
print(list_)
tuple_3 = tuple(list_)
print(tu
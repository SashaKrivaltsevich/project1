def test(spisok):
    return {a: spisok.count(a) for a in set(spisok) if spisok.count(a) > 1}

print(test([1, 1, 3, 4, 4, 6, 4, 3, 5, 3, 1, 3, 11 ]))


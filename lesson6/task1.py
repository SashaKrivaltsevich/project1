def reverse_dict(d):
    d =dict((v, k) for k, v in d.items())
    return d
print(dict(reverse_dict({1: 2, 3: 4, 5: 55})))

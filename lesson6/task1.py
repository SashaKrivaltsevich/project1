dict_ = {'dict': 1, 'dictionary': 2}
print(dict_)
print(dict(reversed(item) for item in dict_.items()))

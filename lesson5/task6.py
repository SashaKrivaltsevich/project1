import timeit
import random

print(timeit.timeit("x = 2 + 2"))

print(timeit.timeit('output = 10*5'))

print(timeit.timeit("x = sum([1, 2, 100, 200, 500])"))

print(timeit.timeit('char in text', setup='text = "sample string"; char = "s"'))

print(timeit.timeit('text.find(char)', setup='text = "sample string"; char = "s"'))

t = timeit.Timer('char in text', setup='text = "sample string"; char = "s"')
print( t.timeit())

def test():
    return random.randint(10, 1000)
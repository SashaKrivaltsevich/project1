n = int(input("Введите число:")) #TODO  фактариал через while

factorial1 = 1
while n > 1:
    factorial1 *= n
    n -= 1


print("Факториал числа равен:")
print(factorial1)

n = int(input("Введите число:"))   #TODO  фактариал через for

factorial_2 = 1
while n > 1:
    factorial_2 *= n
    n -= 1


print("Факториал числа равен:")
print(factorial_2)


def factorial_3(n):   #TODO  фактариал c помощью рекурсии
    if (n <= 1):
        return 1
    else:
        return (n * factorial_3(n-1))

n = int(input("Введите число:"))
print("Факториал числа равен:")
print(factorial_3(n))
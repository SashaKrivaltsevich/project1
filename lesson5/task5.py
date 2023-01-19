from random import randint
a=randint(1,5)
b=int(input("Угадайте целое число от 1 до 5:"))
while b!=a:
    b=int(input("Не угадали))) еще вводи :"))
    if b<a:
        print("Попробуй ввести большее число: ")
    elif b>a and b<5:
        print("Перебор, попробй число поменьше: ")
    elif b > 5:
            print("Написано же, от 1 до 5!!!")
    else:
        print("Вы угадали")


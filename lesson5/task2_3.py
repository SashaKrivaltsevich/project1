name_ = input("entere your name: ")
age_ = int(input("entere your age: "))
while age_ <= 0:
    print("Привет, шкет ", name_)
while age_ > 10 and age_ < 18:
    print("Как жизнь? ", name_)
    while age_ > 18 and age_ < 100:
        print("Что желаете? ", name_)
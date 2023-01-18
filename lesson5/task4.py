value = 1
result = 0
num = int(input("Введите целое число: "))

for item in range(value, num+1):
        result += item ** 3

print(f'Сумма кубов от 1 до введенного числа: {result}')

value = 1
result = 0
while num > 0:
        result += num**3
        num -=1
print(f'Сумма кубов от 1 до введенного числа: {result}')



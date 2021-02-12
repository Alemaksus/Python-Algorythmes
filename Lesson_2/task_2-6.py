# В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать
# не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться, больше или меньше
# введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, вывести ответ.

from random import random
n = round(random() * 100)
i = 1
print("Мы загадали число. Попробуйте его угадать за 10 попыток")
while i <= 10:
    u = int(input(str(i) + '-я попытка: '))
    if u > n:
        print('Меньше')
    elif u < n:
        print('Больше')
    else:
        print('Вы угадали с %d-й попытки' % i)
        break
    i += 1
else:
    print('Увы, но ваши попытки закончились. Число было', n)
# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из
# модуля hashlib задача считается не решённой.

import hashlib

string = input('Введите строку: ')

sum_substr = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        sum_substr.add(hash_str)

print(f'{len(sum_substr) -1} различных подстрок в строке {string}')
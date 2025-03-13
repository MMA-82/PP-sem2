"""Напишите программу, которая получает целое число 
и возвращает его шестнадцатеричное строковое представление. 
Функцию hex используйте для проверки своего результата."""

base16 = 16
chars16 = "0123456789abcdef"

n = int(input('Введите число: '))
print('Оригинал шестнадцатиричный: ',hex(n))
result16 = ''

n_negative = False
if n < 0:
    n_negative = True
    n = -n

while n > base16:
    result16 += chars16[n % base16]
    n //= base16
result16 += str(n)
#result16 = result16 + 'x0'
if n_negative:
        result16 = result16 + 'x0-'
print('Результат совпадает с оригиналом: ',result16[::-1])


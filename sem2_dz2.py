"""Напишите программу, которая принимает две строки вида “a/b” 
- дробь с числителем и знаменателем. 
Программа должна возвращать сумму и произведение* дробей. 
Для проверки своего кода используйте модуль fractions."""
import math
import fractions

drop1 = input('Введите первую дробь вида a/b: ')
drop2 = input('Введите вторую дробь вида a/b: ')

ch1, zn1 = map(int, drop1.split('/'))
ch2, zn2 = map(int, drop2.split('/'))


f_drop1 = fractions.Fraction(ch1, zn1)
f_drop2 = fractions.Fraction(ch2, zn2)

sum_ch = ch1*zn2 + ch2*zn1
prod_ch = ch1*ch2
prod_zn = zn1*zn2

gcd_drop1 = math.gcd(sum_ch, prod_zn)
gcd_ch1 = sum_ch // gcd_drop1
gcd_zn1 = prod_zn // gcd_drop1
gcd_drop2 = math.gcd(prod_ch, prod_zn)
gcd_ch2 = prod_ch // gcd_drop2
gcd_zn2 = prod_zn // gcd_drop2

print(f'Проверочный результат Fraction: сумма = {f_drop1 + f_drop2}, произведение = {f_drop1*f_drop2}')
print(f'Полученные результаты: сумма = {gcd_ch1}/{gcd_zn1}, произведение = {gcd_ch2}/{gcd_zn2}')


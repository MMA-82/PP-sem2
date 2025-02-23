import decimal
import math
decimal.getcontext().prec = 50

while True:
    d = decimal.Decimal(input('Введите желаемый диаметр не более 1000: '))
    if 1 < d < 1000:
        break
pi = decimal.Decimal(math.pi)
s = pi*(d/2)**2
long = 2*pi*(d/2)
print('Площадь круга: ', s)
print('Длина круга: ', long)

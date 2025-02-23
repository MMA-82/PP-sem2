base2 = 2

n = int(input('Введите число: '))
print('Оригинал двоичный: ',bin(n))
result2 = ''
while n > base2:
    result2 += str(n % base2)
    n //= base2
result2 += str(n)
print(result2[::-1])

base8 = 8

n = int(input('Введите число: '))
print('Оригинал восмиричный: ',oct(n))
result8 = ''
while n > base8:
    result8 += str(n % base8)
    n //= base8
result8 += str(n)
print(result8[::-1])
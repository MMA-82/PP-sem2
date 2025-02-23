a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число b: '))

d = b**2 - 4*a*c
if d > 0:
    print((-b + d**0.5)/2*a)
    print((-b - d**0.5)/2*a)
elif d == 0:
     print(-b/2*a)
else:
     d = complex(d)
     print((-b + d**0.5)/2*a)
     print((-b - d**0.5)/2*a)
     
 
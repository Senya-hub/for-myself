a,b,c,d = 8,10,12,18
res = ((-3+a**2)*b-2**3) / (c-2*d)
print('Расчет модели= ', res)

first_quarter = int(input('Введите первое число: '))
second_quarter = int(input('Введите второе число: '))
third_quarter = int(input('Введите третье число: '))
fourth_quarter = int(input('Введите четвертое число: '))
res = (first_quarter+second_quarter) / (third_quarter+fourth_quarter)
print('Динамика дохода = ', res)

number = int(input('Введите число: '))
print('После числа', number, 'идет чило ', number+1)
print('До числа ', number, 'идет число ', number-1)

first_leg = int(input('Введите длину первого катета: '))
second_leg = int(input('Введите длину второго катета: '))
print('Площадь треугольника = ', first_leg*second_leg / 2)

n = int(input('Введите колличество минут: '))
print('Это будет = ', n//60, 'часов и', n%60, 'минут')

first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
print('Сумма: ', (first_number%100) + (second_number%100))

v = int(input('Введите скорость Васи: '))
t = int(input('Введите время Васи: '))
print('Вася остановился: ', v*t % 115, 'километре')

number = int(input('Введите четырехзначное число: '))
print('Первая цифра: ', number//1000)
print('Вторая цифра: ', number//100%10)
print('Третья цифра: ', number//10%10)
print('Последняя цифра: ', number%10)

number = int(input('Введите четырехзначное число: '))
print(number%10, number//10%10, number//100%10, number//1000)

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
print(a, b)
a = str(a)
b = str(b)
a=a+b
b=int(a)//10
a=int(a)%10
print(a, b)
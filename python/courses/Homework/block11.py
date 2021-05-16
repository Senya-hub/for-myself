# Первый пример
bet = int(input('Сколько ставим? '))
coefficient = float(input('Какой коэффициент? '))

win = bet * coefficient

print('Потенциальный выигрыш: ', round(win, 2))

print(win)

win = round(bet * coefficient, 2)

print(win)

# Второй пример про вес
height = float(input('Какой у вас рост? '))
weight = float(input('Какой у вас вес? '))

bmi = round(weight / height ** 2, 2)
print('Ваш индекс равен = ', bmi)

if bmi < 18.5:
  print('У вас недостаточная масса тела')
elif bmi < 25:
  print('У вас нормальная масса тела')
elif bmi < 30:
  print('У вас избыточная масса тела!')
else:
  print('У вас ожирение!')

#Задача 2. День рождения
age = int(input('Введите возраст: '))
t = float(input('Введите температуру? '))

many = round(age * 1.5 * t, 2)
print('Кол-во денег на день рождения: ', many)


# Приведение типа.
while True:
  force = float(input('Введите силу удара: '))
  force *= 10
  print('Балл: ', int(force))
  break

print('Задача 1. Космические рейнджеры\n')
many = float(input('Сколько чатлов? '))

manyCount = many / 2200
print('Это', manyCount, 'CR')
ship = manyCount / 0.5
print('Можно купить кораблей:', int(ship))

print('Задача 2. Компьютерное зрение')
x = float(input('Расположение по горизотали: '))
y = float(input('Расположение по вертикали: '))

if x < 0 or x > 1 or y < 0 or y > 1:
  print('\nКлетки с такой координатой не существует')
else:
  xSquare = (x * 10)
  ySquare = (y * 10)
  print('\nФигура находится в клетке: х = ', int(xSquare), ', y = ', int(ySquare))
print(round(xSquare, 2))
print(round(ySquare, 2))
print('Поправьте положение фигуры на(', )


import math

x = int(input('Введите координату x: '))
y = int(input('Введите координату y: '))

distance = math.sqrt(x ** 2 + y ** 2)
print('Расстояние: ', distance)

import math

distance = int(input('Введите расстояние до танка: '))
angle = int(input('Введите угол в градусах: '))

angle /= 57.2958
x = math.cos(angle) * distance
y = math.sin(angle) * distance

print('Танк находится по координатам: (', x, y, ')')

# Задача 1. Герон
import math

a = int(input('Введите длину стороны а: '))
b = int(input('Введите длину стороны b: '))
c = int(input('Введите длину стороны c: '))

p = (a + b  +c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))

print('Площадь треугольника равна: ', s)

# Задача 2. World of tanks
import math

distance = int(input('Введите расстояние до танка: '))
angle = int(input('Введите угол в градусах: '))

angle /= 57.2958
x = math.cos(angle) * distance
y = math.sin(angle) * distance

print('Танк находится по координатам: (', x, y, ')')



print('Задача 1. Конвертация')
cost = float(input('Введите стоимость покупки в евро: '))

cost_dol = cost * 1.25
cost_rub = cost_dol * 60.87
print('Стоимость покупки', round(cost_rub, 2), 'рубля')


print('Задача 2. Грубая математика')
import math
n = int(input('Введите кол-во чисел: '))
print('\n')

for num in range(1, n + 1):
  print('Введите', num, 'число:', end = ' ')
  count = float(input())
  if count > 0:
    x = math.ceil(count)
    print('x =', x, end = ' ')
    x = math.log(x)
    print('log(x) =', x)
  elif count < 0:
    x = math.floor(count)
    print('x =', x, end = ' ')
    x = math.exp(x)
    print('exp(x) =', x)


print('Задача 3. Убийца Steam')
sizeFile = int(input('Укажите размер файла для скачивания: '))
sizeFile = abs(sizeFile)
connection = int(input('Какова скорость вашего соединения? '))
connection = abs(connection)
print('\n')
count = connection
x = connection

for num in range(1, sizeFile // connection + 1):
  print('Прошло', num, 'сек. Скачено', count, 'из', sizeFile, 'Mb', end = ' ')
  count += connection
  print('(', x,'%)')
  x = count * 100 // sizeFile
print('Прошло', num + 1, 'сек. Скачено', sizeFile, 'из', sizeFile, 'Mb ( 100 %)')


print('Задача 4. Первая цифра')
x = float(input('положительное действительное число X: '))
x = abs(x * 10)
number =(x // 1)
number = (number / 10) 
a = (number // 1)
number = number * 10 - a * 10
print('Первая цифра после десятичной точки -', int(number))


print('Задача 5. Вот это объёмы!')
import math
radius = float(input('Введите радиус случайной планеты: '))
# Надоел английский, хочу как в школе - буковки(хотя бы в одной задаче))
p = math.pi
v = 4 / 3 * p * radius ** 3
z = 10.8321 * (10 ** 11)
if z > v:
  d = (z / v)
  print('Объём планеты Земля больше в', round(d, 3), 'раз')
else:
  l = round(v / z, 3)
  print('Объём планеты Земля меньше в', l, 'раз')


print('Задача 6. Метеостанция')
bottomBound = int(input('Нижняя граница: '))
upperBound = int(input('Верхняя граница: '))
step = int(input('Шаг: '))
print('\n')
y = 0

print('Вывод: ')
print('C    F')
for num in range(0, upperBound // step + 2):
  f = y * 1.8 + 32
  if y < upperBound:
    print(y, '\t', int(f))
    y += step
  else:
    print(upperBound, '\t', int(f))


print('Задача 7. Ход конём')
x = float(input('Введите местоположение коня:\n'))
y = float(input())
a = float(input('Введите местоположение точки на доске:\n'))
b = float(input())

while (x > 0 and x < 0.9) or (y > 0 and y < 0.9): 
  xSquare, ySquare = int(x * 10), int(y * 10)
  aSquare, bSquare = int(a * 10), int(b * 10)
  print('Конь в клетке (', xSquare, ',', ySquare, ').', end = ' ')
  print('Точка в клетке (', aSquare, ',', bSquare,  ').')
  if abs(xSquare - aSquare) == 2 and abs(ySquare - bSquare) == 1:
    print('Да, конь может ходить в эту точку.')
  else:
    print('Нет, конь не может ходить в эту точку.')
  break
else:
  print('Не верно введены коордиаты!')


print('Задача 8. Часы')
hourAngle = float(input('Введите угол(в градусах) с начала часа: '))
print()

minuteAngle = hourAngle % 30 / 30 * 360
print('Минутная стрелка повернулась на', int(minuteAngle), 'градусов.')


print('Задача 9. Уравнение')
import math
a = int(input('Введите значение а: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))
print()

d = b ** 2 - 4 * a * c
print('Дискриминат =', d)
if d > 0:
  rood1 = (-b + math.sqrt(d)) / (2 * a)
  rood2 = (-b - math.sqrt(d)) / (2 * a)
  print('Будет два корня', round(rood1, 3), 'и', round(rood2, 3))
elif d == 0:
  rood = - b / (2 * a)
  print('Корень уравнения равен:', round(rood, 3))
elif d < 0:
  print('если нет корней — не выводите ничего!')


print('Задача 10. За что?')
firstNamber= int(input('Введите первое число: '))
secondNamber = int(input('Введите второе число: '))

bigNamber = (firstNamber + secondNamber + abs(firstNamber - secondNamber)) / 2
print('\nНаибольшее число:', int(bigNamber))


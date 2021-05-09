print('Задача 1. Космическая еда')
i = 0
for porridge in range(100, 0, -4):
  print('Осталось гречки: ', porridge)
  i += 1
print('Гречки хватит на ', i, 'месяцев')

print('Задача 2. Долги')
deptor = int(input('Введите кол-во должников: '))
summ = 0
for number in range(0, deptor, 5):
  print('Должник с номером ', number)
  ask_dept = int(input('Сколько вы должны: '))
  summ += ask_dept
print('Общая сумма долга: ', summ)

print('Задача 3. Это будет бомба')
bomb_time = int(input('Введите кол-во секунд до взрыва: '))
for n in range(bomb_time, -1, -1):
  render = int(input('Хотите обезвредить бомбу? '))
  if render == 0:
    print('До взрыва осталось: ', n)
    if n == 0:
      print('Бомба взорволась!')
  elif render == 1:
    print('Бомба обезврежена! ')
    break
  else:
    print('Бомба взорвалась!')

print('Задача 4. Отрезок')
a = int(input('Введите число а: '))
b = int(input('Введите число b: '))
c = int(input('Введите кратное число с: '))
i = 0
summ = 0
for number in range(a, b + 1, c ):
  print(number)
  summ += number
  i += 1
print('Среднее арифметическое: ', summ // i)

print('Задача 5. Функция 2')
start = int(input('Введите начало отрезка: '))
finish = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))
for x in range(finish, start - 1, step):
  y = x ** 3 + 2 * x ** 2 - 4 * x + 1
  print('В точке', x, 'футкция рава ', y)

print('Задача 6. Письмо')
size = int(input('Введите размер письма: '))
i = 0
for fold in range(size, 0, -1):
  if size < 12:
    print('Отлично, письмо ложим в конверт.')
    break
  print('Надо сложить письмо. Размер большой', size)
  i += 1
  size //=2
print('Надо сложить', i, 'раз!')

print('Задача 7. Стипендия')
educational_grant = int(input('Введите ежемесячную стипендию:'))
summ = 0
expenses = int(input('Введите расходы на проживание:'))
for months in range(1, 11, 1):
  summ += expenses - educational_grant
  print(summ)
  expenses += expenses * 3 // 100
print('У родителей надо взять:', summ)

print('Задача 8. Сумма ряда')
n = int(input('Введите число:'))
s = 0
for number in range(0, n + 1):
  print(number)
  summ =((-1)** number) * (1 /(2 ** number))
  print(summ)
  s += summ
print('S = ', s)

print('Задача 9. Выражение')
x = int(input('Введите число x: '))
summ = x - 1
summ2 = x - 2
for n in range(1, 32, 2):
  summ *=(x -(n * 2 + 1)) 
for d in range(2, 33, 2):
  summ2 *=(x - d * 2)
print('Выражеие =', summ / summ2) 

print('Задача 10. Кинотеатр')
x = int(input('Введите кол-во мальчиков: '))
y = int(input('Введите кол-во девочек: '))
answer = ''
if (x > 2 * y) or (y > 2 * x):
  print('Нет решения!')
elif x >= y:
  k = x - y
  for bgb in range(k):
    answer += "BGB"
  for bg in range(y - k):
    answer += "BG"
else:
  k = y - x
  for gbg in range(k):
    answer += "GBG"
  for gb in range(x - k):
    answer += "GB"
print(answer)
print('Задача 1. Тестовое задание')

for row in range(0, 6):
  for col in range(0, 12, 2):
    print(col + row, end = '\t')
  print()


print('Задача 2. Лестница')
n = int(input('Введите число: '))

for row in range(n + 1):
  for col in range(n + 1):
    if row > col:
      print(row, end = ' ')
  print()


print('Задача 3. Рамка')
width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))

for row in range(width + 1):
  for col in range(height + 1):
    if (col == 0) or (col == height):
      print('|', end = ' ')
    elif (row == 0) or (row == width):
      print('-', end = ' ')
    else:
      print(' ', end = ' ')
  print()


print('Задача 4. Крест')
number = int(input('Введите размер квадрата: '))

for row in range(number + 1):
  for col in range(number + 1):
    if col == row:
      print('^', end = '')
    elif col == -row + number:
      print('^', end = '')
    else:
      print(' ', end = '')
  print()


print('Задача 5. Простые числа')
n = int(input('Введите кол-во чисел:\n '))
numeralCount = 0

for number in range(1, n + 1):
  print('Введите', number, 'чило: ', end = '')
  seqNum = int(input())
  while seqNum > 1:
    if (seqNum % seqNum == 0) and (seqNum % 1 == 0):
      numeralCount += 1
    seqNum = 1
      
print('\nКол-во простых чисел в заданной последовательности:', numeralCount)


print('Задача 6. Сумма факториалов')
n = int(input('Введите число: '))
numeralCount = 1
summ = 0

for number in range(1, n + 1):
  numeralCount *= number
  print('Факториал', number, '=', numeralCount)
  summ += numeralCount
print('Сумма факториалов равна: ', summ)

print('Задача 7. Наибольшая сумма цифр')
n = int(input('Введите кол-во цифр: '))
numeralCount = 0
summ = 0
namber = 0

for number in range(1, n + 1):
  print('Введите', number, 'натуральное чило: ', end = '')
  namberNatural = int(input())
  summ = 0
  for num in range(1, namberNatural + 1):
    summ += num
    if summ > numeralCount:
      numeralCount = summ
      namber =namberNatural
      print(numeralCount)

print('Наибольшее по сумме цифр число:', namber, '. Cумма его цифр: ', numeralCount)


print('Задача 8. Пирамидка\n')
height = int(input('Введите высоту пирамидки: '))

for row in range(height + 1, 0, -1):
  for col in range(0, height + 1):
    if col >= row:
      print('#', end = ' ')
    elif col <= -row + row // 2:
      print('#', end = ' ')
    else:
      print('', end = ' ')
  print()


  print('Задача 9. Пирамидка 2')
level = int(input('Введите кол-во уровней пирамидки: '))
n = 1

for row in range(level + 1, 0, -1):
  for col in range(0, level + 1):
    if col >= row:
      print(n, end = '  ')
      n += 2
    else:
      print('', end = '  ')
  print()


print('Задача 10. Яма ')
n = int(input('Введите число N: '))
print('\n')

print(n)
for row in range(0, n):
  for col in range(0, n * 2):
    if col <= row:
      print(n - col, end = '')
    elif col >= -row + n * 2 - 1:
      print(col - (n - 1), end = '')
    else:
      print('.', end = '')
  print()
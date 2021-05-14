# Таблица умножения
for row in range(1, 10):
  for col in range(1, 10):
    print(row * col, end = '\t')
  print()


# Сумма от 1 до N
n = int(input('Введите число: '))

for i in range(n + 1):
  for a in range(n + 1):
    print(i + a, end = ' ')
  print()

# Анализ данных
for row in range(0, 10):
  for col in range(0, -10, -1):
    print(row + col, end = '\t')
  print()


size = int(input('Введите размер таблицы: '))

for row in range(1, size + 1):
  for col in range(1, size + 1):
    if row % 2 == 0:
      print(row, end = ' ')
    else:
      print(col, end = ' ')
  print()

# Координатные оси
  for row in range(20):
  for col in range(50):
    if row == 9:
      print('-', end = '')
    elif col == 24:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

# Матрица
n = int(input('Введите размер матрицы: '))
for row in range(1, n+1):
  for col in range(1, n+1):
    if row % 2 == 0:
      print(row, end = ' ')
    else:
      print(col, end = ' ')
  print()

# Черный ящик
n = int(input('Введите размер матрицы: '))
for row in range(1, n+1):
  for col in range(1, n+1):
    if col % 3 == 0:
      print(col, end = ' ')
    else:
      print(row, end = ' ')
  print()


  for row in range(size):
  for col in range(size):
    if row < col:
      print('0', end = ' ')
    elif row > col:
      print('2', end = ' ')
    else:
      print('1', end = ' ')
  print()


for row in range(20):
  for col in range(50):
    if row == 9:
      print('-', end = '')
    elif col == row + 29:
      print('\\', end = '')
    elif col == -row + 19:
      print('/', end = '')
    elif col == 24:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

  # Задача 1. Врата
 for row in range(20):
  for col in range(30):
    if row == 0:
      print('-', end = '')
    elif col == 0:
      print('|', end = '')
    elif col == 29:
      print('|', end = '')
    else:
      print(' ', end = '')
  print()

  # Задача 2. Дорога
  for row in range(20):
  for col in range(50):
    if col == row + 29:
      print('\\', end = '')
    elif col == -row + 19:
      print('/', end = '')
    elif col == 24:
      print('|', end = '')
    elif row == 9:
      print('-', end = '')
    else:
      print(' ', end = '')
  print()

# Задача 3. Диагональная матрица 
size = int(input('Введите размер матрицы: '))

for row in range(1, size + 1, 1):
  for col in range(size + 1, 1, -1):
    if col > row + 1:
      print('0', end = ' ')
    elif col < row + 1:
      print('2', end = ' ')
    else:
      print('1', end = ' ')
  print()  



people = int(input('Введите кол-во людей: '))

for hour in range(people + 1):
  print('Идет час:', hour)
  for num in range(hour, people):
    print('Номер в очереди: ', num)
  print()
print('Очередь обслужена!')

seqNum = int(input('Сколько будет чисел: '))
numeral = int(input('Какую цифру считать? '))
while numeral < 0 or numeral > 9:
  numeral = int(input('Цифра должна быть в дифпазоне от 0 до 9. Введите новую цифру: '))
numeralCount = 0
for num in range(seqNum):
  print('Введите', num, 'число: ', end = '')
  number = int(input())
  while number > 0:
    if number % 10 == numeral:
      numeralCount += 1
    number //= 10
print('Цифр', numeral, 'в последовательности:', numeralCount) 

# Задача 2. Цифры больше пяти
seqNum = int(input('Сколько будет чисел: '))
numeralCount = 0

for num in range(seqNum):
  print('Введите', num, 'число: ', end = '')
  number = int(input())
  while number > 0:
    if number % 10 > 5:
      numeralCount += 1
    number //= 10
print('Общее кол-во цифр больше 5 в последовательности:', numeralCount)  

# Задача 3. Лестница чисел
number = int(input('Введите число: '))

for row in range(number):
  #print(row, end = '')
  for col in range(number):
    print(row, end = '')
    #print(col, end = '')
  print()


for number in range(1, 4):
  pincode = int(input('Введите пин-код: '))
  if pincode == 1234:
    print('Пин-код верный! Получите вашу зарплату!')
    break
  print('Неверный пин-код. Осталось попыток: ', 3 - number)
else:
  print('Ваша карта заблокирована! До свидания.')

while True:
  for number in range(1, 4):
    pincode = int(input('Введите пин-код: '))
    if pincode == 1234:
      print('\nПин-код верный! Получите вашу зарплату!\n')
      break
    print('Неверный пин-код. Осталось попыток: ', 3 - number)
  else:
    print('\nВаша карта заблокирована! До свидания.\n')
  print('Следующий клиент. Добро пожаловать!') 
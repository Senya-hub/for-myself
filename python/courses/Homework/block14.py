# Нахождение простого числа
number = int(input('Введите число: '))
banner = True
for num in range(2, number):
  if number % num == 0:
    banner = False
    break
if banner:
  print('Число простое.') 
else:
  print('Число составное.')

# Повторение цикла for
for row in range(1, 10):
  for col in range(1, 10):
    print(row * col, end = '\t')
  print()
print('\n')

for row in range(5):
  for col in range(5):
    print(row + col, end = '\t')
  print()
print('\n')

for row in range(0, 6, 2):
  for col in range(6):
    print(row, end = '\t')
  print()


print('Задача 2. Калькулятор\n')
# скрипт для ком. строки

def count(actos, f_number, s_number):
  c = 0
  if actos == '+':
    c = f_number + s_number 
  elif actos == '-':
    c = f_number - s_number
  elif actos == '*':
    c = f_number * s_number
  elif actos == '/':
    c = f_number / s_number 
  print('\n', f_number, actos, s_number, '=', int(c))
  
while True:
  actos = input('\nВыберите операцию: ')
  f_number = int(input('Введите первое число: '))
  s_number = int(input('Введите второе число: '))
  if actos == '+':
    count(actos, f_number, s_number)
    break
  elif actos == '-':
    count(actos, f_number, s_number)
    break
  elif actos == '*':
    count(actos, f_number, s_number)
    break
  elif actos == '/':
    count(actos, f_number, s_number)
    break
  else: 
    print('Ошибка: такой операции не существует. Попробуйте ещё раз.')



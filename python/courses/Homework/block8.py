# Возведение в квадрат
n = int(input('Введите число: '))
for number in range(n//2 + 1):
  number *= 2
  print(number, '** 2 ', number ** 2)

# Деление клеток
total_hours = int(input('Введите кол-во часов: '))
cells = 1
for hour in range(1, total_hours // 3 + 1):
  cells *= 2
  print('Прошло часов: ', hour * 3)
  print('Клеток: ', cells)
  print('Часов до конца эксперемента: ', total_hours - hour * 3)
  print()
print('Наблюдение завершено!')

# Квадраты нечестных чисел
n = int(input('Введите число: '))
for number in range(1, n + 1, 2):
  print(number, '** 2 ', number ** 2)

# Куб нечетного числа в диапазоне пользователя
number = int(input('Введите размер диапазона: '))
for n in range(1, number + 1, 2):
  print(n, '** 3 = ', n ** 3)

# Сумма каждого пятого числа введенного диапазона
n = int(input('Введите кол-во стульев в зале: '))
summ = 0
for number in range(1, n + 1, 5):
  print('Номер стула:', number)
  summ += number
print('Сумма: ', summ)

# Подсчет воды и калорий
wake_up = int(input('Саша проснулся в: '))
water = 0
calories = 0
for hour in range(wake_up, 23, 3):
  water += 1
  ate_calories = int(input('Сколько калорий съел? '))
  calories += ate_calories
print('Выпьет воды: ', water)
print('Съест калорий: ', calories)

# Прятки
times = int(input('Введите кол-во секуд: '))
for t in range(times, 0, -1):
  print(t)
print('Я иду искать!')

# Сколько правил в уставе
total_soldiers = int(input('Введите кол-во солдат в шеренге: '))
total_rules = int(input('Введите кол-во правил в уставе: '))
push_ups = 0
for ask in range(total_soldiers, 0, -4):
  rules = int(input('Сколько правил в уставе?'))
  if total_rules != rules:
    print('Неправильно! ', ask * 10, 'Отжиманий!')
    push_ups += 10 * ask
print('Общее кол-во отжиманий =', push_ups)

# Прятки(хитрость)
times = int(input('Введите кол-во секуд: '))
for t in range(times, 0, -2):
  print(t)
print('Я иду искать!')